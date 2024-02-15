from os import getenv
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = getenv("OPENAI_API_KEY")

class ImageGenerator:
    def __init__(self, model, prompt):
        self.client = OpenAI()
        self.model = model
        self.prompt = prompt

    def generate(self):
        response = self.client.images.generate(
        model=self.model,
        prompt=self.prompt,
        size="1024x1024",
        quality="standard",
        n=1,
        )
        return response
    
    def display_url(self, response):
        return response.data[0].url
