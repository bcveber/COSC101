# ----------------------------------------------------------
# HW 03: Image Manipulation with functions
# ----------------------------------------------------------
# Please answer these questions after having completed the
# entire assignment.
# ----------------------------------------------------------
# Name:
#
# Hours spent in total:
#
# Collaborators (if any):
#
# Feedback: What was the hardest part of this assignment?
#   <your answer here>
#
# Feedback: Any suggestions for improving the assignment?
#   <your answer here>
# ----------------------------------------------------------



import cImage as image


# -------------------------------
# EXAMPLE FUNCTION: RED FILTER
# -------------------------------
# Here is an example of a transformation function. Note that this
# function is called from the main() function below.

def red_filter(img):
    """ (Image object) -> Image object
    Returns a copy of img where the blue and green have been filtered
    out and only red remains.
    """
    red_only_img = img.copy() # create copy to manipulate
    w = img.getWidth()
    h = img.getHeight()
    for x in range(w): # iterate through all (x, y) pixel pairs
        for y in range(h):
            pixel = img.getPixel(x, y)
            red = pixel.getRed() # get original red value
            redPixel = image.Pixel(red, 0, 0)
            red_only_img.setPixel(x, y, redPixel) # replace pixel
    return red_only_img # return filtered image




#--------------------------------
# BEGIN GRADED FUNCTIONS
#--------------------------------
# Fill in docstrings and code for all of the functions required by the
# homework assignment. For your convenience, each of the function
# definitions have been started for you. However, note that all of the
# functions are currently defined to take zero parameters and return
# None. You will need to change this for (at least) some of these
# functions.

def grayscale(img):
    ''' ( ) -> NoneType
    Description here.
    '''
    grayscale_img = img.copy()
    w = img.getWidth()
    h = img.getHeight()
    for x in range(w):
        for y in range(h):
            pixel = img.getPixel(x,y)
            
            red = pixel.getRed()
            green = pixel.getGreen()
            blue = pixel.getBlue()

            avg = int((red + green + blue) / 3)
            
            newpixel = image.Pixel(avg, avg, avg)
            grayscale_img.setPixel(x,y,newpixel)
            
    return grayscale_img
            
    

def cycle_colors(img):
    ''' ( ) -> NoneType
    Description here.
    '''
    cycle_colors_img = img.copy()
    w = img.getWidth()
    h = img.getHeight()
    for x in range(w):
        for y in range(h):
            pixel = img.getPixel(x,y)
            
            red = pixel.getRed()
            green = pixel.getGreen()
            blue = pixel.getBlue()

            newpixel = image.Pixel(pixel.getGreen(), pixel.getBlue(), pixel.getRed())
            cycle_colors_img.setPixel(x,y,newpixel)

    return cycle_colors_img
            

def negative(img):
    ''' ( ) -> NoneType
    Description here.
    '''
    negative_img = img.copy()
    w = img.getWidth()
    h = img.getHeight()
    for x in range(w):
        for y in range(h):
            pixel = img.getPixel(x,y)
            
            Red = pixel.getRed()
            Green = pixel.getGreen()
            Blue = pixel.getBlue()

            newpixel = image.Pixel(abs(pixel.getRed()-255), abs(pixel.getGreen()-255), abs(pixel.getBlue()-255))
            negative_img.setPixel(x,y,newpixel)

    return negative_img

def brightness(img,increase_decrease):
    ''' ( ) -> NoneType
    Description here.
    '''
    brightness_img = img.copy()
    w = img.getWidth()
    h = img.getHeight()
    for x in range(w):
        for y in range(h):
            pixel = img.getPixel(x,y)

            red = pixel.getRed()
            green = pixel.getGreen()
            blue = pixel.getBlue()
            
            Red = pixel.getRed() + increase_decrease
            Blue = pixel.getBlue() + increase_decrease
            Green = pixel.getGreen() + increase_decrease

            if Blue > 255:
                Blue = 255
            if Blue < 0:
                Blue = 0
            if Red > 255:
                Red = 255
            if Red < 0:
                Red = 0
            if Green > 255:
                Green = 255
            if Green < 0:
                Green = 0

            newpixel = image.Pixel(Red, Green, Blue)
            brightness_img.setPixel(x,y,newpixel)

    return brightness_img           

def increase_contrast(img):
    ''' ( ) -> NoneType
    Description here.
    '''
    increase_contrast_img = img.copy()
    w = img.getWidth()
    h = img.getHeight()
    for x in range(w):
        for y in range(h):
            pixel = img.getPixel(x,y)

            red = pixel.getRed()
            green = pixel.getGreen()
            blue = pixel.getBlue()
            
            if red == 128:
                red = red
            if red > 128:
               red = 128 + ((red - 128) * 2)
            if red < 128:
                red = 128 + ((red-128) * 2)
            if red > 255:
                red = 255
            if red < 0:
                red = 0

            if blue == 128:
                blue = blue
            if blue > 128:
               blue = 128 + ((blue - 128) * 2)
            if blue < 128:
                blue = 128 + ((blue-128) * 2)
            if blue > 255:
                blue = 255
            if blue < 0:
                blue = 0

            if green == 128:
                green = green
            if green > 128:
               green = 128 + ((green - 128) * 2)
            if green < 128:
                green = 128 + ((green-128) * 2)
            if green > 255:
                green = 255
            if green < 0:
                green = 0

            newpixel = image.Pixel(red, green, blue)
            increase_contrast_img.setPixel(x,y,newpixel)

    return increase_contrast_img          

def posterize(img):
    ''' ( ) -> NoneType
    Description here.
    '''
    posterize_img = img.copy()
    w = img.getWidth()
    h = img.getHeight()
    for x in range(w):
        for y in range(h):
            pixel = img.getPixel(x,y)

            red = pixel.getRed()
            green = pixel.getGreen()
            blue = pixel.getBlue()
            
            if red %32 != 0:
                red = red-(red%32)
            if red > 255:
                red = 255
            if red < 0:
                red = 0

            if blue %32 != 0:                
                blue = blue-(blue%32)
            if blue > 255:
                blue = 255
            if blue < 0:
                blue = 0

            if green %32 != 0:                
                green = green-(green%32)
            if green > 255:
                green = 255
            if green < 0:
                green = 0

            newpixel = image.Pixel(red, green, blue)
            posterize_img.setPixel(x,y,newpixel)

    
    return posterize_img

def vertical_flip(img):
    ''' ( ) -> NoneType
    Description here.
    '''
    vertical_flip_image = img.copy()
    w = img.getWidth()
    h = img.getHeight()
    for x in range(w):
        for y in range(h):
            pixel = img.getPixel(x,h-1-y)

            red = pixel.getRed()
            green = pixel.getGreen()
            blue = pixel.getBlue()

            newpixel = image.Pixel(red,green,blue)
            vertical_flip_image.setPixel(x,y,newpixel)
    return vertical_flip_image

def horizontal_mirror(img):
    ''' ( ) -> NoneType
    Description here.
    '''
    horizontal_mirror_image = img.copy()
    w = img.getWidth()
    h = img.getHeight()
    for x in range(w//2):
        for y in range(h):
            pixel = img.getPixel(x,y)

            red = pixel.getRed()
            green = pixel.getGreen()
            blue = pixel.getBlue()
            
            newpixel = image.Pixel(red,green,blue)
            horizontal_mirror_image.setPixel((w-1)-x,y,newpixel)

    return horizontal_mirror_image

def scroll(img,total_shift):
    ''' ( ) -> NoneType
    Description here.
    '''
    scroll_image = img.copy()
    w = img.getWidth()
    h = img.getHeight()
    for x in range(w):
        for y in range(h):
            pixel = img.getPixel(x,y)
            
            red = pixel.getRed()
            green = pixel.getGreen()
            blue = pixel.getBlue()
    
            newpixel = img.getPixel((x+total_shift) % w, y)
            scroll_image.setPixel(x,y,newpixel)
    return scroll_image

def obamafy(img):
    ''' ( ) -> NoneType
        Description here.
    '''

    obamafy_image = img.copy()
    w = img.getWidth()
    h = img.getHeight()
    for x in range(w):
        for y in range(h):
            pixel = img.getPixel(x,y)

            red = pixel.getRed()
            green = pixel.getGreen()
            blue = pixel.getBlue()
            
            
            total_color = int((red + green + blue) / 3)

            yellow = image.Pixel(252,227,166)
            darkblue = image.Pixel(0,51,76)
            lightblue = image.Pixel(112,150,158)
            obamared = image.Pixel(217,26,33)
            
            if total_color <= 121 and total_color >= 61:
                obamafy_image.setPixel(x,y,obamared)
            if total_color >= 182:
                obamafy_image.setPixel(x,y,yellow)
            if total_color <= 60:
                obamafy_image.setPixel(x,y,darkblue)
            if total_color <= 182 and total_color >=122:
                obamafy_image.setPixel(x,y,lightblue)

    return obamafy_image

def save_image(image,file):
    ''' ( ) -> NoneType
    Description here.
    '''
    image_tosave = image.save(file)

    return image_tosave

def save_images(images,files):
    ''' ( ) -> NoneType
    Description here.
    '''
    for i in range(len(images)):
        save_image(images[i], files[i])
        
    return images

#--------------------------------
# BEGIN MAIN FUNCTION
#--------------------------------
# Replace the code below to call all of the transformation functions
# you wrote display and save the results. Your main should call every
# graded function you wrote above. You can test your code using the
# provided crayons.gif file or another .gif image of your choosing, as
# long as the image file is in the same directory as this .py file.
def main():
    """ () -> NoneType
    Main Program that load image(s) from file(s) and performs
    transformations to those images as required for HW 03. The images
    are then displayed.
    """
    original_img = image.Image('pres_casey.gif')
    red_image = red_filter(original_img)
    win = image.ImageWin(original_img.getWidth(), original_img.getHeight())
    red_image.draw(win)

    grayscale_img = grayscale(original_img)
    grayscale_img.draw(win)

    cycle_colors_img = cycle_colors(original_img)
    cycle_colors_img.draw(win)

    negative_img = negative(original_img)
    negative_img.draw(win)

    brightness_img = brightness(original_img, 90)
    brightness_img.draw(win)

    increase_contrast_img = increase_contrast(original_img)
    increase_contrast_img.draw(win)

    vertical_flip_image = vertical_flip(original_img)
    vertical_flip_image.draw(win)

    posterize_image = posterize(original_img)
    posterize_image.draw(win)

    scroll_image = scroll(original_img, 10)
    scroll_image.draw(win)

    horizontal_mirror_image = horizontal_mirror(original_img)
    horizontal_mirror_image.draw(win)

    obamafy_image = obamafy(original_img)
    obamafy_image.draw(win)


# To test your code you will run this program and then enter:
#       >>> main()
# at the shell. Do not include an uncommented call to main() here.
