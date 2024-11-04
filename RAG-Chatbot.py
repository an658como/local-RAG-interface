# Importing the modules
import os
import SLM
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.memory import ConversationBufferWindowMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.agents import Tool, initialize_agent

# Initialize LocalLLM with the specified endpoint URL
llm = SLM.LocalLLM(endpoint_url="http://localhost:5001/chat")

#import serpapi
os.environ["SERPAPI_API_KEY"] = "4e7c0c06f2695b2f953f8ba029a82b5662b171937dd352be5a9ea1d7633fae8f"


# Loading the document
loader = PyPDFLoader("3DPrinter_Manual.pdf")
mypdf = loader.load() 

# Defining the splitter 
document_splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=70
)

# Splitting the document into chunks
docs = document_splitter.split_documents(mypdf)

# Embedding the chunks into vector stores
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Setting the directory for storing vector data
persist_directory = 'db'

# Initialize Chroma vector store from documents
my_database = Chroma.from_documents(
    documents=docs,
    embedding=embeddings,
    persist_directory=persist_directory
)

# Defining the conversational memory
retaining_memory = ConversationBufferWindowMemory(
    memory_key='chat_history',
    k=5,
    return_messages=True
)

# Defining the conversational retrieval chain with retriever and memory
question_answering = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=my_database.as_retriever(),
    memory=retaining_memory
)

# defining the tool for the agent
tools = [
    Tool(
        name='Knowledge Base',
        func=question_answering.run,
        description=(
            'use this tool when answering questions related to the 3D printer'
        )
    )
]

# initializing the agent
agent = initialize_agent(
    agent='chat-conversational-react-description',
    tools=tools,
    llm=llm,
    verbose=True,
    max_iterations=3,
    early_stopping_method='generate',
    memory=retaining_memory
)

# Loop for a conversation with the AI
while True:
    question = input("Enter your query: ")
    if question.lower() == 'escape': 
        break 
    print(agent(question))