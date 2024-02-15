# Image Generator with OpenAI API
The ImageGenerator class is a Python module designed for generating images using the OpenAI API based on textual prompts and a specified model.

## Features
Generate Images: Create images using a specified model and text prompt.
Easy to Use: Simple and straightforward interface for image generation.
Customizable: Can be extended and modified for more complex use cases.
## Requirements
Before you get started, you will need:

Python 3.x
openai Python library
An active subscription to OpenAI and the API key.
## Installation
Install Python Dependencies: You need to have Python installed on your system. The project is tested on Python 3.x.

Install Required Libraries:

```
pip install openai python-dotenv
```
Environment Setup:

Create a .env file in your project root directory.
Add your OpenAI API key to this file:
```
OPENAI_API_KEY=your_api_key_here
```
## Usage
```
from img_generator import ImageGenerator

input_1 = input("Ton modèle ?  ") # dall-e-3 (for example)
input_2 = input("Ton prompt ?  ")

img = ImageGenerator(input_1, input_2)
response = img.generate()
print(img.display_url(response))
```

## Disclaimer
This project and its developers are not affiliated with OpenAI. Please use OpenAI services according to their guidelines and terms of service.