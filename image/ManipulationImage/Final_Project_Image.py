
from PIL import Image
image_beach = Image.open(r"C:\Users\exmarcsd\Documents\Python\image\ManipulationImage\Images\beach.jpg")
image_cactus = Image.open(r"C:\Users\exmarcsd\Documents\Python\image\ManipulationImage\Images\cactus.jpg")

#1. Verify the image size
print(image_beach.size)
#2. Verify the image format
print(image_beach.format)
#3. Create new image background
#background = Image.new("RGB", image_beach.size)
#4. Get pixels Image Cactus
#pixels_cactus = image_cactus.load()
#5. Get pixels color value position Cactus
#(r, g, b) = pixels_cactus[200,200]
#6. Get pixels Image position Blackground
#pixels_new = background.load()
#7. Set color at pixels
#pixels_new[100,200] = (r, g, b)
#print(pixels_new[10,10])

for y in range(0,600):
    for x in range(0,600):
        #4. Get pixels Image Cactus
        pixels_cactus = image_cactus.load()
        #5. Get pixels color value position Cactus
        (r, g, b) = pixels_cactus[y,x]
        if (r!=76 and b!=24): 
            #6. Get pixels Image position Blackground
            pixels_new = image_beach.load()
            #7. Set color at pixels
            pixels_new[y,x] = (r, g, b)      

#image_beach.show()



image_beach.save("cactus_edit.jpg")