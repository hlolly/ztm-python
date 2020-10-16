import sys
import os
from PIL import Image

pokedex_folder = sys.argv[1]
new_folder = sys.argv[2]

if not os.path.exists(new_folder):
    os.makedirs(new_folder)

for image in os.listdir(pokedex_folder):
    pokemon = Image.open(f'{pokedex_folder}{image}')
    image2 = os.path.splitext(image)[0]
    pokemon.save(f'{new_folder}{image2}.png', 'png')
