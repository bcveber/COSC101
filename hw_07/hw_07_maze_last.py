# ----------------------------------------------------------
# --------               HW 7: Maze                ---------
# ----------------------------------------------------------

# ----------------------------------------------------------
# Please answer these questions after having completed this
# program
# ----------------------------------------------------------
# Name: Brian Veber
# Hours spent on program: literally 12
# Collaborators and sources: Tutors (Wed. and Thurs.), Brodie Cohen, Tyler Petrone, Matthew Copeland
#   (List any collaborators or sources here.)
# ----------------------------------------------------------


# Complete your code for the maze program here
# Define and use any helper functions you want/need!

def row_col_move(row, column, maze):
    '''
    (str, str, list) --> (str, str, list)
    Tries up, down, left, and right movements in the maze. Will run through if equal to 'O'
    '''
    if maze[row][column + 1] == 'O': #Rightwards movement for function in maze
        column += 1 
        return row, column, maze
    if maze[row - 1][column] == 'O': #Upwards movement for function in maze
        row -= 1
        return row, column, maze
    if maze[row + 1][column] == 'O': #Downwards movement for function in maze
        row += 1 #print (row)
        return row, column, maze
    elif maze[row][column - 1] == 'O': #Leftward movement for function in maze
        column -= 1 #print (column)
        return row, column, maze
    #print (row, column, maze) -- tester

def leftmaze(row, column, maze):
    '''
    (int, int, list) ----> (T/F)
    Leftward movement.
    '''
    if maze[row][column-1] == ' ': #moves left
        return True
    else:
        return False #returns left if the left doesnt work
    
def rightmaze(row, column, maze):
    '''
    (int, int, list) ----> (T/F)
    rightward movement.
    '''
    if maze[row][column + 1] == ' ': #moves right
        return True
    else:
        return False #returns false if the right doesnt work
    
def downmaze(row, column, maze):
    '''
    (int, int, list) ----> (T/F)
    downward movement.
    '''
    if maze[row + 1][column] == ' ': #moves down
        return True
    else:
        return False #returns false if the down doesnt work

def upmaze(row, column, maze):
    '''
    upward movement.
    (int, int, list) ----> (T/F)
    '''
    if maze[row - 1][column] == ' ': #moves up
        return True
    else:
        return False #returns false if the up doesn't work
    
def maze_movement(row, column, maze):
    '''
    (int, int, list) ---> (list)
    Uses the above functions to run through the maze. Returns the letters
    according to their movements, and then runs through recurisvely again on
    the maze to check the next movement.
    '''
    
    spot = maze[0] #set spot to the maze
    row_spot = len(maze) - row #adjust row
    column_spot = len(spot) - column #adjust column

    if column == len(spot) - 1 and len(maze) - 2: #returns empty list
            return []
    if upmaze(row, column, maze) > 0: 
        if row > 0:
            maze[row][column] = 'O' #will produce a U if the upmaze function works with the indexing
            row -= 1
        return ['U'] + maze_movement(row, column, maze)
    if downmaze(row, column, maze) > 0: 
        if row_spot > 0:
            maze[row][column] = 'O' #will produce a D if the upmaze function works with the indexing
            row += 1
            #print (row) --- test
        return ['D'] + maze_movement(row, column, maze)
    if leftmaze(row, column, maze) > 0:
        if column > 0:
            maze[row][column] = 'O' #will produce a L if the upmaze function works with the indexing
            column -= 1
            #print (column) --- test
        return ['L'] + maze_movement(row, column, maze)
    if rightmaze(row, column, maze) > 0:
        if column_spot > 0:
            #print (column_spot) -- test
            maze[row][column] = 'O' #will produce a R if the upmaze function works with the indexing
            column += 1

            return ['R'] + maze_movement(row, column, maze)
    else:
        maze[row][column] = 'X' #X on the maze
        row, column, maze = row_col_move(row, column, maze) #new variables
        return ['Block'] + maze_movement(row, column, maze) #Block stands for a block in the maze, its stuck

def solve(maze):
    mazelist = maze_movement(1, 0, maze) #Runs through the maze and collects the list of letters
    mazemovements = ''
    for x in range(len(mazelist)):
        if mazelist[x] == 'Block': #Goes through any blocks in the maze
            mazemovements = mazemovements[:-1]
        else:
            mazemovements += mazelist[x] #adds the final maze
            
    mazemovements += 'R' #Adds a final right move to end the maze
    #print (mazemovements) #tester
            
    return mazemovements #returns final movements
            
            
        
            

        
    
    
    
#----------------------------------------------------------------------------------
# If, when you execute "Run Module" in IDLE or when you run this script,
# you want to automatically run the main() function, which
# prompts for a filename, loads the maze, and then calls your solve()
# method to try and solve it, then change this line to True

run_main = True



#----------------------------------------------------------------------------------
# Don't change the code below this line

def load_maze(filename):
    ''' (str) -> list of lists of strings
        Returns a table representing the maze in the given filename '''
        
    try:
        f = open(filename)
        maze = []
        for line in f:
            if 'X' in line:
                maze.append(list(line[:-1]))
        f.close()
        return maze

    except IOError:
        return None

def main():
    filename = input('Enter maze filename to load: ')
    maze = load_maze(filename)
    if maze is None:
        print('Error opening', filename)
        return
    else:
        path = solve(maze).upper()
        print('Maze solved.  The solution is:')
        print(path)


if __name__ == '__main__' and run_main:
    main()
