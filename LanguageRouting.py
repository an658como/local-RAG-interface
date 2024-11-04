'''
1.Create destination chains for each of the following languages: French, Spanish, Dutch, and Italian.
2.Create a default chain when no language mentioned in task 1 is identified.
3.Create the router chain
'''
# importing LangChain modules
import SLM
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.prompts import ChatPromptTemplate
from langchain.chains.router import MultiPromptChain
from langchain.chains.router.llm_router import LLMRouterChain,RouterOutputParser
from langchain.chains.router.multi_prompt_prompt import MULTI_PROMPT_ROUTER_TEMPLATE

llm = SLM.LocalLLM(endpoint_url="http://localhost:5001/chat")

# Defining prompt templates for the destination chains 
french_template = """You are proficient in the French language and are very knowledgeable. \
 Translate the customer query to English and then respond to the user in French. \
 Be polite and have a friendly tone. \

Here is a question:
{input}"""

spanish_template = """You are proficient in the Spanish language and are very knowledgeable. \
 Translate the user query to English and then respond to the user in Spanish. \
 Be polite and have a friendly tone. \

Here is a question:
{input}"""

dutch_template = """You are proficient in the Dutch language and are very knowledgeable. \
 Translate the user query to English and then respond to the user in Dutch. \
 Be polite and have a friendly tone. \

Here is a question:
{input}"""

italian_template = """You are proficient in the Italian language and are very knowledgeable. \
 Translate the user query to English and then respond to the user in Italian. \
 Be polite and have a friendly tone. \

Here is a question:
{input}"""

# store your prompt templates in prompt_infos here
prompt_infos = [
    {
        "name": "French",
        "description": "Good for answering questions in French", #field helps the router chain decide when to use the destination chain.
        "prompt_template": french_template
    },
    {
        "name": "Spanish",
        "description": "Good for answering questions in Spanish",
        "prompt_template": spanish_template
    },
    {
        "name": "Dutch",
        "description": "Good for answering questions in Dutch",
        "prompt_template": dutch_template
    },
    {
        "name": "Italian",
        "description": "Good for answering questions in Italian",
        "prompt_template": italian_template
    }
]

destination_chains = {}
for p_info in prompt_infos:
    name = p_info["name"]
    prompt_template = p_info["prompt_template"]
    prompt = ChatPromptTemplate.from_template(template=prompt_template)
    chain = LLMChain(llm=llm, prompt=prompt)
    destination_chains[name] = chain

destinations = [f"{p['name']}: {p['description']}" for p in prompt_infos]
destinations_str = "\n".join(destinations)

# create the default chain here
default_prompt = ChatPromptTemplate.from_template("{input}")
default_chain = LLMChain(llm=llm, prompt=default_prompt)

router_template = MULTI_PROMPT_ROUTER_TEMPLATE.format(
    destinations=destinations_str
)

# define the router prompt here
router_prompt = PromptTemplate(
    template=router_template,
    input_variables=["input"],
    output_parser=RouterOutputParser(),
)

# create the router chain here
router_chain = LLMRouterChain.from_llm(llm, router_prompt)


final_chain = MultiPromptChain(router_chain=router_chain,
                         destination_chains=destination_chains,
                         default_chain=default_chain, verbose=True
                        )

# write your query here
print(final_chain.run("Wat is de beste manier om snel een nieuwe taal te leren?"))