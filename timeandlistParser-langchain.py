from langchain.prompts import PromptTemplate
from langchain.output_parsers import DatetimeOutputParser, CommaSeparatedListOutputParser
from pydantic import BaseModel, Field
import SLM

# Initialize the local LLM
llm = SLM.LocalLLM(endpoint_url="http://localhost:5001/chat")

# Set up the output parsers
parser_dateTime = DatetimeOutputParser()
parser_List = CommaSeparatedListOutputParser()

# Create the prompt template
template = """Provide the response in format {format_instructions} 
to the user's question: {question}"""

# Create prompt templates for datetime and list parsing
prompt_dateTime = PromptTemplate.from_template(
    template,
    partial_variables={"format_instructions": parser_dateTime.get_format_instructions()},
)

prompt_List = PromptTemplate.from_template(
    template,
    partial_variables={"format_instructions": parser_List.get_format_instructions()},
)

# Format the prompts
formatted_prompt_dateTime = prompt_dateTime.format(question="When was the first iPhone launched?")
formatted_prompt_List = prompt_List.format(question="What are the four famous chocolate brands?")

# Query the local LLM
response_dateTime = llm.invoke(formatted_prompt_dateTime)
response_list = llm.invoke(formatted_prompt_List)

# Print the responses
print(response_dateTime)
print(response_list)

'''
1701-10-08T20:20:02.473206Z
1439-01-07T16:42:11.400024Z
0456-11-27T21:44:49.063938Z
Milk Duds, Hershey's, Snickers, 3 Musketeers
'''