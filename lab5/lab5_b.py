#Brian Veber, Lab05, Lab5_a

import cImage as image


#Create an Image object from the file 
img = image.Image('secret_message.gif')
#Create a copy that we will change
redCopy = img.copy()

#Return the width of the image in pixels
w = img.getWidth()
#Return the height of the image in pixels
h = img.getHeight()

col = 0
row = 0
green_blue = 0

for col in range (w):
    for row in range (h):
        pixel = img.getPixel(col, row)

        #RGB values of the pixel 
        red = pixel.getRed()
        green = pixel.getGreen()
        blue = pixel.getBlue()

        if red == 13:
            green_blue = green + blue
            chr(green_blue)
print(green_blue)














win = image.ImageWin(redCopy.getWidth(), redCopy.getHeight())
redCopy.draw(win)
win.exitonclick()

redCopy.save('secret_message.gif')

