import openai
import Functions

class ollama():
    def __init__(self, model:str, command:str):
        self.model = model
        self.command = command
    
    def chat(self):
        client = openai.OpenAI(
            base_url="http://localhost:11434/v1",
            api_key="nokeyneeded",
        )

        response = client.chat.completions.create(
            model=self.model, #the model that has already been pulled
            temperature=0.7, #a parameter to control the randomness of the response (this should be a number between 0 to 2)
            n=2, # number of responses
            messages=[
                {"role": "system", "content": "helpful assistant!"},
                {"role": "user", "content": self.command},
            ],
        )
        response_text = response.choices[0].message.content
        
        Functions.justify_text(response_text)