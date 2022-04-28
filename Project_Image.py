
from PIL import Image
image_beach = Image.open("beach.jpg")
print(image_beach.size)
print(image_beach.format)
pixels_beach = image_beach.load()
print(pixels_beach[200,100])

for y in range(100,500):
    for x in range(0,300):
        (r, g, b) = pixels_beach[x,y]
        new_blue = b +50
        pixels_beach[x,y] = (r, g, new_blue)

image_beach.show()

#image_beach.save("testeazul.jpg")
