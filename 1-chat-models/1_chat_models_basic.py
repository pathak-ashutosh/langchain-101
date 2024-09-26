from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load environment variables from .env
load_dotenv()

# Get a model instance
model = ChatOpenAI(model='gpt-4o')

# Use the invoke method to get a response
result = model.invoke('How many prime numbers there are between 1 and 100?')

print("Full Result:")
print(result)
print("Only Content:")
print(result.content)