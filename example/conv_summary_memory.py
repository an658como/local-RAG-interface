'''
A concise summary of the interaction is often sufficient to
store the context. The ConversationSummaryMemory module
stores a summary of the interactions over time instead
of keeping all or a limited number of past interactions.
This method is advantageous for longer conversations,
efficiently storing key information over time without
overwhelming the model with excessive storage requirements.
'''
# importing LangChain modules
from langchain.memory import ConversationSummaryMemory
from langchain.chains import ConversationChain
import slm

# Initialize LocalLLM with the specified endpoint URL
llm = slm.local_llm(endpoint_url="http://localhost:5001/chat")

memory = ConversationSummaryMemory(llm=llm)

memory.save_context({input: "Alex is a 9-year old boy."}, 
                    {"output": "Hello Alex! How can I assist you today?"})
memory.save_context({input: "Alex likes to play football"}, 
                    {"output": "That's great to hear! "})

conversation = ConversationChain(
    llm=llm,
    memory = memory, #the memory set’s context through the previously defined conversation memory buffer.
    verbose=True #The verbose options allow us to visualize the internal workings of the model
)

print(conversation.predict(input="How old is Alex?"))