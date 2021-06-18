from PIL import Image
image_original = Image.open("beach.jpg")
image_second = Image.open("penguin.jpg")

width1, height1 = image_original.size
width2, height2 = image_second.size

pixels_original = image_original.load()
pixels_second = image_second.load()

#r1, g1, b1 = pixels_original
#image_original.show()



image_new = Image.new("RGB", image_original.size)
pixels_new = image_new.load()

for x in range (width2):
    for y in range (height2):
        r2, g2, b2 = pixels_second[x, y]
        if r2 < 100 and g2 > 200 and b2 < 75:
            pixels_new[x, y] = pixels_original[x, y]
        else:
            pixels_new[x, y] = pixels_second[x, y]
    

image_new.show()
image_new.save("the_new_image.jpg")
