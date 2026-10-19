import sys
from rembg import remove
from PIL import Image

input_path = 'profile.png'
output_path = 'profile_cutout.png'

print(f"Loading {input_path}...")
input_image = Image.open(input_path)

print("Removing background with AI model...")
output_image = remove(input_image)

print(f"Saving transparent cutout to {output_path}...")
output_image.save(output_path, format="PNG")
print("Background successfully removed!")
