from os import getenv
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = getenv("OPENAI_API_KEY")

class ImageGenerator:
    """
    A class for generating images using OpenAI's API based on given prompts and model.
    """
    def __init__(self, model, prompt):
        """
        Initializes the image generator with a specific model and text prompt.

        :param model: The name of the model to use for generating images.
        :param prompt: The text prompt based on which the image will be generated.
        """
        self.client = OpenAI()
        self.model = model
        self.prompt = prompt

    def generate(self):
        """
        Generates an image based on the initialized model and prompt.

        :return: The API response containing the generated image.
        """
        response = self.client.images.generate(
        model=self.model,
        prompt=self.prompt,
        size="1024x1024",
        quality="standard",
        n=1,
        )
        return response
    
    def display_url(self, response):
        """
        Extracts and returns the URL of the generated image from the API response.

        :param response: The API response from which the image URL is to be extracted.
        :return: The URL of the generated image.
        """
        return response.data[0].url
