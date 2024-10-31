import SLM
from pydantic import BaseModel

# Initialize LocalLLM instance
llm = SLM.LocalLLM(endpoint_url="http://localhost:5001/chat")

# Define message types to replicate SystemMessage and HumanMessage behavior
class Message(BaseModel):
    role: str  # "system" or "user"
    content: str

# Define messages with roles to simulate conversation
messages = [
    Message(role="system", content="You are a math tutor who provides answers with a bit of sarcasm."),
    Message(role="user", content="What is the square of 2?"),
]

# Combine messages into a single prompt string
prompt = "\n".join([f"{message.role}: {message.content}" for message in messages])

# Query the model and print the response
response = llm._call(prompt)  # Directly calling _call here to send the combined prompt
print(response)