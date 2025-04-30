import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from langchain.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
import os

# Set Streamlit app title
st.set_page_config(page_title="📈 Mutual Fund Optimization App", layout="wide")
st.title("📈 Mutual Fund Optimization App")

# Load FAISS Vector Database
@st.cache_data
def load_vector_db():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    faiss_index = FAISS.load_local(
        "C:/Users/KIIT/OneDrive/Desktop/FINANCE_AI/Mutual_fund/docs/faiss_rag",
        embeddings,
        allow_dangerous_deserialization=True  # ✅ Fix for deserialization error
    )
    return faiss_index

# Initialize FAISS index
faiss_index = load_vector_db()

# Load LLM (Groq)
groq_api_key = os.getenv("GROQ_API_KEY")  # Ensure your API key is set
llm = ChatGroq(
    groq_api_key=groq_api_key,
    model_name='gemma2-9b-it',
    temperature=0.1
)

# Prompt Template
template = """
Based on the following mutual fund data, analyze and provide optimization recommendations in Sector Wise Percentages only for Each Fund.
Mutual Fund Information: {query}
Context: {context}
Answer:
"""
PROMPT = PromptTemplate(input_variables=["context", "query"], template=template)

# Set up Retriever & QA Chain
retriever = faiss_index.as_retriever(search_kwargs={"k": 5})

qa_chain = RetrievalQA.from_chain_type(
    llm, retriever=retriever, chain_type_kwargs={"prompt": PROMPT}
)

# Remove Duplicates from Documents
def remove_duplicates(documents):
    seen = set()
    unique_docs = []
    for doc in documents:
        if doc.page_content not in seen:
            unique_docs.append(doc)
            seen.add(doc.page_content)
    return unique_docs

# Get Optimized Recommendations
def get_optimized_recommendations(query):
    raw_docs = retriever.get_relevant_documents(query)
    unique_docs = remove_duplicates(raw_docs)
    context = " ".join([doc.page_content for doc in unique_docs])
    result = qa_chain({"context": context, "query": query})
    return result

# Sidebar Input
st.sidebar.header("📊 Optimization Query")
query = st.sidebar.text_input("Enter your query:", "Analyze and provide optimization recommended percentages for each sector.")

if st.sidebar.button("Get Recommendations"):
    response = get_optimized_recommendations(query)
    st.success("✅ Optimization Recommendations:")
    st.write(response['result'])

# Example Data for Visualization
original_data = {
    'Fund_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Tech_Exposure_%': [18.65, 21.57, 25.82, 26.27, 26.89, 16.40, 20.23, 49.10, 47.85, 32.10],
    'Healthcare_Exposure_%': [16.37, 44.54, 49.24, 40.05, 20.65, 33.60, 37.80, 19.71, 34.87, 11.30],
    'Finance_Exposure_%': [23.75, 29.63, 17.51, 12.29, 16.51, 22.81, 10.02, 22.37, 45.57, 36.83],
    'Energy_Exposure_%': [10.25, 13.50, 16.82, 18.84, 15.54, 6.44, 6.91, 9.80, 8.79, 15.19]
}

optimized_data = {
    'Fund_ID': [8, 3, 6, 9, 5],
    'Tech_Exposure_%': [35, 20, 10, 40, 20],
    'Healthcare_Exposure_%': [19.71, 60, 40, 25, 30],
    'Finance_Exposure_%': [15, 15, 15, 30, 15],
    'Energy_Exposure_%': [15, 5, 5, 5, 5]
}

# DataFrames
original_df = pd.DataFrame(original_data)
optimized_df = pd.DataFrame(optimized_data)

# Merge DataFrames
merged_df = pd.merge(original_df, optimized_df, on='Fund_ID', suffixes=('_Original', '_Optimized'))

# Melt DataFrame for Plotting
melted_df = pd.melt(
    merged_df, 
    id_vars=['Fund_ID'], 
    value_vars=[
        'Tech_Exposure_%_Original', 'Healthcare_Exposure_%_Original',
        'Finance_Exposure_%_Original', 'Energy_Exposure_%_Original',
        'Tech_Exposure_%_Optimized', 'Healthcare_Exposure_%_Optimized',
        'Finance_Exposure_%_Optimized', 'Energy_Exposure_%_Optimized'
    ],
    var_name='Type', value_name='Exposure'
)

# Extract Sector & Optimization Type
melted_df['Sector'] = melted_df['Type'].apply(lambda x: x.split('_')[0])
melted_df['Optimization'] = melted_df['Type'].apply(lambda x: 'Original' if 'Original' in x else 'Optimized')

# Visualization
st.subheader("📊 Sector Exposure: Original vs Optimized")

plt.figure(figsize=(14, 8))
sns.barplot(data=melted_df, x='Fund_ID', y='Exposure', hue='Optimization', palette='Set2', ci=None)
plt.title('Original vs Optimized Sector Exposure for Each Fund')
plt.xlabel('Fund ID')
plt.ylabel('Exposure (%)')
plt.legend(title='Optimization')
plt.xticks(rotation=45)
plt.tight_layout()

st.pyplot(plt.gcf())
