from phi.agent import Agent
from phi.model.groq import Groq
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
os.environ['GROQ_API_KEY'] = os.getenv("GROQ_API_KEY")

agent=Agent(id="llama-3.3-70b-versatile")

agent.print_response("Write a short story on king")