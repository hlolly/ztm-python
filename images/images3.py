from PIL import Image, ImageOps

# Open image
im = Image.open('./8201.jpg')

# Add border and save
bordered = ImageOps.expand(im, border=10, fill=(0,0,0))

bordered.save('result.png')