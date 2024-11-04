# importing LangChain modules
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
import SLM

# Initialize LocalLLM with the specified endpoint URL
llm = SLM.LocalLLM(endpoint_url="http://localhost:5001/chat")

memory = ConversationBufferMemory()
memory.save_context({input: "Alex is a 9-year old boy."}, 
                    {"output": "Hello Alex! How can I assist you today?"})
memory.save_context({input: "Alex likes to play football"}, 
                    {"output": "That's great to hear! "})

conversation = ConversationChain(
    llm=llm,
    memory = memory, #the memory set’s context through the previously defined conversation memory buffer.
    verbose=True #The verbose options allow us to visualize the internal workings of the model
)

print(conversation.predict(input="don't greet, jut tell me How old is Alex?"))