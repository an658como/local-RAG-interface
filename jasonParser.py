import SLM
from typing import List
from pydantic import BaseModel, Field
from langchain.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser

llm = SLM.LocalLLM(endpoint_url="http://localhost:5001/chat")
# Define the Author class for the output
class Book(BaseModel):
    title: str
    author: str

class Author(BaseModel):
    number: int = Field(description="Number of books written by the author")
    books: List[Book] = Field(description="List of books written by the author")

# User query
user_query = "Generate a list of books written by Dan Brown and the total number."

# Define the output parser
output_parser = PydanticOutputParser(pydantic_object=Author)

# Define the prompt template
prompt = PromptTemplate(
    template=(
        "You are a helpful assistant. Answer the following question in a valid JSON format "
        "matching this structure: {format_instructions}.\n\n"
        "Make sure the response contains only the data, not the schema.\n\n"
        "{query}"
    ),
    input_variables=["query"],
    partial_variables={"format_instructions": output_parser.get_format_instructions()},
)

# Generate the formatted prompt
my_prompt = prompt.format_prompt(query=user_query)

# Send the prompt to the model and retrieve the output
output = llm.invoke(my_prompt.to_string())

# Print the raw output for debugging
print("Raw Output:", output)

# Parse the output and print the result
try:
    parsed_output = output_parser.parse(output)
    print(parsed_output)
except Exception as e:
    print(f"Error parsing output: {e}")