import slm
import os
# importing LangChain modules
from langchain.llms import OpenAI
from langchain.agents import AgentType, initialize_agent, load_tools

os.environ["SERPAPI_API_KEY"] = "YOUR_API_KEY"

# Initialize LocalLLM with the specified endpoint URL
llm = slm.local_llm(endpoint_url="http://localhost:5001/chat")

# loading tools
tools = load_tools(["serpapi", 
                    "llm-math"], 
                    llm=llm)

agent = initialize_agent(tools, 
                        llm, 
                        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, 
                        verbose=True)

# user's query
print(agent.run("who is Mehran Dadsetan?"))