import streamlit as st
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.schema import HumanMessage
from langchain_groq import ChatGroq
from langchain_community.embeddings import HuggingFaceEmbeddings
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
os.environ['GROQ_API_KEY'] = os.getenv("GROQ_API_KEY")

# Load FAISS index
faiss_path_bank = "C:/Users/KIIT/OneDrive/Desktop/FINANCE_AI/Personalized_Chatbot/docs/faiss_rag"

# Load embeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Load FAISS index with dangerous deserialization enabled
faiss_index_bank = FAISS.load_local(faiss_path_bank, embeddings, allow_dangerous_deserialization=True)

# Groq API setup
llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name='gemma2-9b-it',
    temperature=0.1
)

# Prompt Template
template = """
You are a Finance QNA Expert. Analyze the Query and Respond to the Customer with a suitable answer within 150 words. If you don't know the answer, just say "Sorry, I don't know."
Question: {question}
Context: {context}
Answer:
"""
PROMPT = PromptTemplate(input_variables=["context", "query"], template=template)

# Create retriever
retriever_bank = faiss_index_bank.as_retriever(search_kwargs={"k": 1})

# Define QA Chain
qa_chain_bank = RetrievalQA.from_chain_type(llm, retriever=retriever_bank, chain_type_kwargs={"prompt": PROMPT})

# Streamlit UI
st.title("GenAI Financial Chatbot")
st.write("Ask your finance-related questions.")

# User input
user_query = st.text_input("Ask your question:", "")

# Chat Response
if st.button("Get Answer") and user_query:
    context = "Your context here"  # Update if needed
    try:
        result = qa_chain_bank({"context": context, "query": user_query})
        st.markdown(f"**Question:** {user_query}")
        st.markdown(f"**Answer:** {result['result']}")  # Limit answer to 150 characters
    except RuntimeError as e:
        st.error(f"RuntimeError encountered: {e}")
