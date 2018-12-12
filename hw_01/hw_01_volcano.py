# ----------------------------------------------------------
# --------              HW 1: Volcano              ---------
# ----------------------------------------------------------

# ----------------------------------------------------------
# Please answer these questions after having completed this
# program
# ----------------------------------------------------------
# Name:  Brian Veber
# Hours spent on program 2: 3 hours
# Collaborators and sources:
#   (List any collaborators or sources here.)
# ----------------------------------------------------------


# write your python program for the volcano problem here

#Brian Veber, Volcano

#Identify the scale

scale = int(input('To what scale will your volcano be?'))
new_scale = scale * 3

#Create the loop of spaces and parantheses using variable x (fumes of volcano)

for i in range(scale, 0, -1):
    s = ' '
    x = (new_scale + i + 1) * s + '(' + scale * ' ' + i * '  ' + ')'
    print(x)

x = (new_scale + 1) * ' ' + '(' + scale * '_' + ')'
print(x)

#Create the loop of A's and / using variable y (head of volcano)

for i in range(0, new_scale):
    y = ' ' * (new_scale - i)
    y = y + '/' + 'A' * (scale + i * 2 + 1)
    print(y + '\\')
