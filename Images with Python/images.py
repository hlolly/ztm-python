from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')
filtered_img = img.filter(ImageFilter.BLUR)
filtered_img2 = img.filter(ImageFilter.SMOOTH)
filtered_img3 = img.filter(ImageFilter.SHARPEN)
convert_img = img.convert('L')
crooked = img.rotate(90)
resize = img.resize((300, 300))
box = (100, 100, 400, 400)
crop = img.crop(box)


print(img.format)
print(img.size)
print(img.mode)
#print(dir(img))


filtered_img.save("blur.png", 'png')
filtered_img2.save("smooth.png", 'png')
filtered_img3.save("sharpen.png", 'png')
convert_img.save("grey.png", 'png')
filtered_img3.show()
crooked.save("crooked.png", 'png')
resize.save("resize.png", 'png')
crop.save("crop.png", 'png')