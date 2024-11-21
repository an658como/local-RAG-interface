import os
# importing LangChain modules
from langchain.memory import ConversationBufferMemory
from langchain.agents import AgentType, initialize_agent, load_tools
import slm

os.environ["SERPAPI_API_KEY"] = "YOUR_API_KEY"

#Initialize LocalLLM with the specified endpoint URL
llm = slm.local_llm(endpoint_url="http://localhost:5001/chat")

memory = ConversationBufferMemory(memory_key="chat_history")

# loading tools
tools = load_tools(["serpapi"], 
                    llm=llm)

agent = initialize_agent(tools,
                        llm,
                        agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
                        verbose=True,
                        memory=memory)

agent.run("Hi, my name is Alex, and I live in the New York City.")
agent.run("My favorite game is basketball.")
print(agent.run("Give me the list of stadiums to watch a basketball game in my city today. Also give the teams that are playing."))