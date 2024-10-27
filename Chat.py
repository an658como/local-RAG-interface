import SLM

SLM_model = SLM.ollama("llama3.2:1b", "tell me a joke")
SLM_model.chat()
