from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import slm

llm = slm.local_llm(endpoint_url="http://localhost:5001/chat")

# creating the prompt template
prompt_template = PromptTemplate(
    input_variables=["pet"],
    template="A very popular breed of {pet}?",
)

# creating the chain
chain = LLMChain(llm=llm, 
                prompt=prompt_template, 
                verbose=True)

# calling the chain
print(chain.run("Cat"))

