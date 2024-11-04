# Importing the modules
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.memory import ConversationBufferWindowMemory  # Fixed import path
from langchain.chains import ConversationalRetrievalChain
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
import SLM

# Initialize LocalLLM with the specified endpoint URL
llm = SLM.LocalLLM(endpoint_url="http://localhost:5001/chat")

# Loading the document
loader = PyPDFLoader("story.pdf")
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

# Loop for a conversation with the AI
while True:
    question = input("Enter your query: ")
    if question.lower() == 'escape': 
        break 
    # Getting the response, ensuring context is emphasized
    result = question_answering({"question": f"Answer only in the context of the document provided: {question}"})
    print(result['answer'])