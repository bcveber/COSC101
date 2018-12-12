#Brian Veber, Volcano

#Identify the scale


scale = int(input('To what scale will your volcano be?'))
new_scale = scale * 3

#Create the loop of spaces and parantheses using x

for i in range(scale, 0, -1):
    s = ' '
    k = (new_scale + i + 1) * s + '(' + scale * ' ' + i * '  ' + ')'
    print(k)

k = (new_scale + 1) * ' ' + '(' + scale * '_' + ')'
print(k)

#Create the loop of A's and / using variable y

for i in range(0, new_scale):
    a = ' ' * (new_scale - i)
    a = a + '/' + 'A' * (scale + i * 2 + 1)
    print(a + '\\')
