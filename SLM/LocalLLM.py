from langchain.llms.base import LLM
from pydantic import Field
import requests

class LocalLLM(LLM):
    endpoint_url: str = Field(..., description="URL of the local LLM server")

    def _call(self, prompt: str, stop=None) -> str:
        response = requests.post(self.endpoint_url, json={"prompt": prompt})
        if response.status_code == 200:
            return response.json().get("response")
        else:
            raise ValueError(f"Error {response.status_code}: {response.text}")

    @property
    def _identifying_params(self):
        return {"endpoint_url": self.endpoint_url}

    @property
    def _llm_type(self):
        return "local_llm"