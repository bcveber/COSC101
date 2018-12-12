# Island Generation program
# by Vijay Ramachandran
#    Computer Science
#    Colgate University

import random

empty = '~'
full = 'X'
p = 0.35

def generate(rows, cols):
    s = ''
    for i in range(rows):
        row = ''
        for j in range(cols):
            if random.random() < p:
                row += full
            else:
                row += empty
        row += '\n'
        s += row
    return s

def main():
    rows = int(input('Enter number of rows: '))
    cols = int(input('Enter number of columns: '))
    islands = generate(rows, cols)
    print('Generated.')
    disp = input('Do you want to display the map (y/n)? ').lower()
    if disp.startswith('y'):
        print(islands)
    save = input('Do you want to save the map (y/n)? ').lower()
    if save.startswith('y'):
        filename = input('Enter filename: ')
        with open(filename, 'w') as f:
            f.write(islands)
            f.close()
            
if __name__ == '__main__':
    main()
