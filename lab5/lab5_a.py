#Brian Veber, Lab05, Lab5_a

import cImage as image


#Create an Image object from the file 
img = image.Image('scramble.gif')
#Create a copy that we will change
redCopy = img.copy()

#Return the width of the image in pixels
w = img.getWidth()
#Return the height of the image in pixels
h = img.getHeight()

col = 0
row = 0

for col in range (w):
    for row in range (h):
        pixel = img.getPixel(col, row)

        #RGB values of the pixel 
        red = pixel.getRed()
        green = pixel.getGreen()
        blue = pixel.getBlue()

        # Add Green at multiples of 25 into the pixel
        newPixel = image.Pixel(0, green*25, 0)
        redCopy.setPixel(col, row, newPixel)
        row = row + 1
    col = col + 1
    row = 0


win = image.ImageWin(redCopy.getWidth(), redCopy.getHeight())
redCopy.draw(win)
win.exitonclick()

redCopy.save('scramble.gif')

