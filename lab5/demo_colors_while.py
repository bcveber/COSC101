#Brian Veber, Lab05

import cImage as image


#Create an Image object from the file 
img = image.Image('colors.gif')
#Create a copy that we will change
redCopy = img.copy()

#Return the width of the image in pixels
w = img.getWidth()
#Return the height of the image in pixels
h = img.getHeight()

col = 0
row = 0

while col < w:
    while row < h:
        pixel = img.getPixel(col, row)

        #RGB values of the pixel 
        red = pixel.getRed()
        green = pixel.getGreen()
        blue = pixel.getBlue()

        # filter out green and blue in new pixel
        newPixel = image.Pixel(red, 0, 0)

        redCopy.setPixel( col, row, newPixel)
        row = row + 1
    col = col + 1
    row = 0
        



# use while loops to iterate over every (col,row) pair
# follow the demo_colors.py example which uses a for nested loop










win = image.ImageWin(redCopy.getWidth(), redCopy.getHeight())
redCopy.draw(win)
win.exitonclick()

redCopy.save('copy.gif')

