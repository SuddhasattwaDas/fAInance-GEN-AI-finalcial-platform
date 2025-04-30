from phi.agent import Agent
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Fetch the Groq API key
groq_api_key = os.getenv("GROQ_API_KEY")

# Check if the Groq API key was loaded correctly
if not groq_api_key:
    raise ValueError("GROQ_API_KEY not found in environment variables.")

# Bypass OpenAI API requirement with a dummy key
os.environ['OPENAI_API_KEY'] = 'dummy_key'

# Initialize the Agent with the Groq model
agent = Agent(groq_api_key=groq_api_key, id="gemma2-9b-it")

# Get the response from the agent
agent.print_response("Write a short story on a king")
