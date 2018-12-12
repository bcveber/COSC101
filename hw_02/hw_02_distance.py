# ----------------------------------------------------------
# --------          HW 2: Earth Distance           ---------
# ----------------------------------------------------------

# ----------------------------------------------------------
# Please answer these questions after having completed this
# program
# ----------------------------------------------------------
# Name:  Brian Veber
# Hours spent on program 2: 
# Collaborators and sources:
#   (List any collaborators or sources here.)
# ----------------------------------------------------------


# Write your python program for the earth distance problem here

import geocode
import math

R = 6373
D = 0

first_location = input ("Enter the first location: ")
second_location = input ("Enter the second location: ")

loc = geocode.Location(first_location)
first_address = (loc.address())
lat1 = math.radians(loc.lat())
lng1 = math.radians(loc.lng())

loc = geocode.Location(second_location)
second_address = (loc.address())
lat2 = math.radians(loc.lat())
lng2 = math.radians(loc.lng())

x = lat2 - lat1
y = lng2 - lng1
a = (math.sin(x/2))**2 + math.cos(lat1) * math.cos(lat2) * (math.sin(y/2))**2
c = 2 * math.asin(min(1, math.sqrt(a)))
D = R * c

print ("The first location matched the address: ")
print(first_address)
print ("The second location matched the address: ")
print(second_address)
print("The distance between them is", D, "km")

