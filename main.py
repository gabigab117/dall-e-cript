# dall-e-3
from img_generator import ImageGenerator

input_1 = input("Ton modèle ?  ")
input_2 = input("Ton prompt ?  ")

img = ImageGenerator(input_1, input_2)
response = img.generate()
print(img.display_url(response))