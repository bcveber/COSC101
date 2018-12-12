# ----------------------------------------------------------
# --------              HW 7: Island               ---------
# ----------------------------------------------------------

# ----------------------------------------------------------
# Please answer these questions after having completed this
# program
# ----------------------------------------------------------
# Name: Brian Veber (This one was submitted on time, see submission 15 at Apr 28 3:14pm)
# Hours spent on program: 6
# Collaborators and sources: Tutors (Wen. and Thurs.), Brodie Cohen, Shamarcus Doty
#   (List any collaborators or sources here.)
# ----------------------------------------------------------


# Complete your code for the island program here
# Define and write and helper functions you want/need!

def island_searcher(terr, used, row, column):
    '''
    All shell testing done through the island_count function
    ---
    Through if statements and recursion, the function checks for unique
    sets of islands (denoted 'X'). If there is a disconnect in an island,
    then a new island is accounted for. It does not count duplicate islands.
    '''
    
    used[row][column] = 0 #Create island located variable

    if column + 1 < len(terr[0]): #Checks a new column space
        #print (column)
        if row < len(terr):
            #print (row)
            if used[row][column + 1] == 'X':
                #print (used)
                if terr[row][column+1] == 'X': #Checks for new island mark
                    island_searcher(terr, used, row, column + 1) #Recursive function runs if it has found another part of an attached island
                    
    if column - 1 >= 0: #Checks a new column space
        if row < len(terr):
            #print (row)
            if used[row][column-1] == 'X':
                if terr[row][column-1] == 'X': #Checks for new island mark
                    island_searcher(terr, used, row, column - 1)
                    
    if column < len(terr[0]):
        #print (column)
        #print (row)
        if row + 1 < len(terr): #Checks a new row space
            if used[row+1][column] == 'X':
                if terr[row + 1][column] == 'X': #Checks for new island mark
                    island_searcher(terr, used, row + 1, column)
                    
    if column < len(terr[0]):
        if row-1 > 0: #Checks a new row space
            if used[row-1][column] == 'X':
                if terr[row-1][column] == 'X': #Checks for new island mark
                    island_searcher(terr, used, row - 1, column)
    
def island_count(terr):
    '''
    Goes through the rows and columns in the given island set and runs the
    island_searcher program to find the total number of unique islands, which
    is returned by 'islandcount.'
    ---
    Testing:
    Enter islands filename to load: islands_7x15.txt
    8 island(s)
    Enter islands filename to load: islands_6x6.txt
    5 island(s)
    '''
    used = terr[:] #Set used variable
    islandcount = 0 #Set island count
    
    for row in range(len(used)): #Runs through rows
        for column in range(len(used[row])): #Runs through columns
            if used[row][column] == 'X': #Checks for island markers
                islandcount += 1
                #print (islandcount)
                island_searcher(terr, used, row, column) #Runs through island_searcher to check what part of an island the marker is

    return islandcount #Returns island count

#----------------------------------------------------------------------------------
# If, when you execute "Run Module" in IDLE or when you run this script,
# you want to automatically run the main() function, which
# prompts for a filename, loads the map, and then calls your island_count
# function, then change this line to True

run_main = True


#----------------------------------------------------------------------------------
# Don't change the code below this line

def load_terr(filename):
    ''' (str) -> list of lists of strings
        Returns a table representing the grid of ~ and X in the given filename '''
        
    try:
        f = open(filename)
        terr = []
        for line in f:
            if len(line.strip()) > 0:
                terr.append(list(line[:-1]))
        f.close()
        return terr

    except IOError:
        return None

def main():
    filename = input('Enter islands filename to load: ')
    terr = load_terr(filename)
    if terr is None:
        print('Error opening', filename)
        return
    else:
        count = island_count(terr)
        print(count, 'island(s)')


if __name__ == '__main__' and run_main:
    main()

