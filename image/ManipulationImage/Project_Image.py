
from PIL import Image
image_beach = Image.open(r"C:\Users\exmarcsd\Documents\Python\image\ManipulationImage\Images\cactus.jpg")
print(image_beach.size)
print(image_beach.format)
pixels_beach = image_beach.load()
print(pixels_beach[200,213])

for y in range(100,300):
    for x in range(200,213):
        (r, g, b) = pixels_beach[x,y]
        #new_blue = b +50
        pixels_beach[x,y] = (r, g, 104)
        print(pixels_beach[x,y])
    

image_beach.show()

#image_beach.save("testeazul.jpg")
