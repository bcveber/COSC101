# ----------------------------------------------------------
# --------              HW 1: Shapes               ---------
# ----------------------------------------------------------

# ----------------------------------------------------------
# Please answer these questions after having completed this
# program
# ----------------------------------------------------------
# Name: Brian Veber
# Hours spent on program 2: 1.5 hour
# Collaborators and sources:
#   (List any collaborators or sources here.)
# ----------------------------------------------------------


# Write your python program for the shapes problem here

#Brian Veber, Shapes

#import math in order to use square root of 3

import math

#Area of Circle

radius = float(input("Circle radius: "))
area = str(radius*radius*3.14159)
print("Your circle has an area of", area+".") 

#Area of Square

square = float(input("Square side length: "))
square_area = str(square * square)              
print("Your square has an area of", square_area+".")

#Area of Equilateral Triangle

equilateral_length = float(input("Equilateral triangle side length: "))
equilateral_area = str((math.sqrt(3)*equilateral_length*equilateral_length)/4)
print("Your triangle has an area of", equilateral_area+".")

#Tested all 4 examples, as well as unique numbers such as 100 and 0.
