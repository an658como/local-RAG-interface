import SLM
import os
# importing LangChain modules
from langchain.llms import OpenAI
from langchain.agents import AgentType, initialize_agent, load_tools

os.environ["SERPAPI_API_KEY"] = "4e7c0c06f2695b2f953f8ba029a82b5662b171937dd352be5a9ea1d7633fae8f"

# Initialize LocalLLM with the specified endpoint URL
llm = SLM.LocalLLM(endpoint_url="http://localhost:5001/chat")

# loading tools
tools = load_tools(["serpapi", 
                    "llm-math"], 
                    llm=llm)

agent = initialize_agent(tools, 
                        llm, 
                        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, 
                        verbose=True)

# user's query
print(agent.run("What is the current population of the world, and calculate the percentage change compared to the population five years ago"))