import slm

# Initialize LocalLLM with the specified endpoint URL
llm = slm.local_llm(endpoint_url="http://localhost:5001/chat")

# Directly call _call with your prompt
response = llm("Tell me a joke")
print("Response from model:", response)