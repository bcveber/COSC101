# Maze Generation program
# by Vijay Ramachandran
#    Computer Science
#    Colgate University

import random

class DisjointSets:
    
    def __init__(self, n):
        self.s = [-1] * n
        
    def __repr__(self):
        return repr(self.s)
        
    def __len__(self):
        return len(self.s)
        
    def count(self):
        return sum([1 if x < 0 else 0 for x in self.s])
        
    def find(self, x):
        if self.s[x] < 0: return x
        else:
            self.s[x] = self.find(self.s[x])
            return self.s[x]
    
    def union(self, x, y):
        r_x = self.find(x)
        r_y = self.find(y)
        
        if r_x == r_y: return -1
        
        if self.s[r_x] < self.s[r_y]:
            larger = r_x
            smaller = r_y
        else:
            larger = r_y
            smaller = r_x
        
        self.s[larger] += self.s[smaller]
        self.s[smaller] = larger
        
        return -self.s[larger]
        
class Maze:

    ch = 'X'

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols        
        self.generate()

    def generate(self):
    
        rows = self.rows
        cols = self.cols
    
        total = rows * cols
    
        d = DisjointSets(total)
        right = [True] * total
        bot = [True] * total
    
        right[-1] = False
        
        walls = total*2-rows-cols
        per_row = (cols-1)*2 + 1
        last_row = cols-1
        
        choices = list(range(walls))
        random.shuffle(choices)
    
        while d.count() > 1:
            x = choices.pop()
            
            if x >= walls-last_row:
                row = rows-1
                col = x - (walls-last_row)
                cell = row*cols + col
                if d.union(cell, cell+1) != -1:
                    right[cell] = False
            else:
                row = x // per_row
                col = (x % per_row) // 2
                dir = (x % per_row) % 2
                cell = row*cols + col
                if col == cols-1 or dir == 0:
                    if d.union(cell, cell+cols) != -1:
                        bot[cell] = False
                else:
                    if d.union(cell, cell+1) != -1:
                        right[cell] = False
    
        self.right = right
        self.bot = bot

    def __repr__(self):
        
        s = ''
        
        # top wall
        s += Maze.ch * (self.cols * 2 + 1) + '\n'
        
        for row in range(self.rows):
            s += (' ' if row == 0 else Maze.ch)
            for col in range(self.cols):
                s += ' '
                s += (Maze.ch if self.right[row*self.cols + col] else ' ')
            s += '\n' + Maze.ch
            for col in range(self.cols):
                s += ((Maze.ch * 2) if self.bot[row*self.cols + col] else (' ' + Maze.ch))
            s += '\n'
        
        return s
        
    def save(self, filename):
        with open(filename, 'w') as f:
            f.write(repr(self))
        f.close()
        
def main():
    print('This program will generate a random maze.')
    rows = int(input('How many rows (odd integer >= 3)? '))
    cols = int(input('How many columns (odd integer >= 3)? '))
    m = Maze(rows//2,cols//2)
    print('Maze generated.')
    disp = input('Would you like to display it (y/n)? ').lower()
    if disp.startswith('y'):
        print(m)
    save = input('Would you like to save this maze (y/n)? ').lower()
    if save.startswith('y'):
        filename = input('Enter filename: ')
        m.save(filename)
    print('Finished.')

if __name__ == '__main__':
    main()
