from langchain.prompts.few_shot import FewShotPromptTemplate
from langchain.prompts import PromptTemplate
import SLM

llm = SLM.LocalLLM(endpoint_url="http://localhost:5001/chat")
# Define few-shot examples with more explicit instructions
examples = [
    {"review": "I absolutely love this product! It exceeded my expectations.", "sentiment": "Sentiment: Positive"},
    {"review": "I'm really disappointed with the quality of this item. It didn't meet my needs.", "sentiment": "Sentiment: Negative"},
    {"review": "The product is okay, but there's room for improvement.", "sentiment": "Sentiment: Neutral"},
]

# Adjust template for each example
example_prompt = PromptTemplate(
    input_variables=["review", "sentiment"],
    template="Review: {review}\n{sentiment}"
)

# Adjust the few-shot prompt template to explicitly instruct the model
prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix="Given the following reviews and their sentiments, classify the sentiment of the new review in the same way:\n\n",
    suffix="Review: {input}\nSentiment:",
    input_variables=["input"]
)

# Format the prompt
message = prompt.format(input="The machine worked okay without much trouble.")

# Query the model with the updated prompt
response = llm._call(message)
print("Response from model:", response)