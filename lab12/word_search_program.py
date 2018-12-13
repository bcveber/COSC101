# ----------------------------------------------------------
# Lab 12
# Cosc 101
# Spring 2017

#Matt Copeland, Brian Veber
# ----------------------------------------------------------


#imports all the function of word_search_functions
from word_search_functions import *  

#MAKE SURE both .py files are
# * located in the directory and
# * SAVED before you run this file

def get_num_rows(puz):
    """ (str) -> int

    Return the number of rows in puzzle, which is a game board.

    >>> get_num_rows('abcd\nefgh\nijkl\n')
    3
    """
    rows = 0 #assign row value
    for letter in puz: #runs through letters
        if letter == "\n":
            rows += 1
    return rows #returns puzzle rows

#Independent Function Tests
#print ("get_num_rows test: dummy return")
#print (get_num_rows('abcd\nefgh\nijkl\n'))


def get_num_cols(puz):
    """ (str) -> int

    Return the number of columns in puzzle, which is a game board.

    >>> get_num_cols('abcd\nefgh\nijkl\n')
    4
    """
    columns = 0 #assing col value   
    for letter in puz: #runs through letters
        if letter == "\n":
            break 
        columns += 1
        
    return columns #returns puzzle columns

#Independent Function Tests
#print ("get_num_cols test: dummy return")
#print (get_num_cols('abcd\nefgh\nijkl\n'))

def print_puzzle(puz):
    """ (str) -> NoneType

    Print the puzzle with row and column numbers and two spaces
    between each letter.
    """
    num_rows = get_num_rows(puz)        # Gets the amount of rows in the puzzle
    num_columns = get_num_cols(puz)      # Gets the amount of colummns in the puzzle


    # ADD code to print the column headings.
    print("    ", end = '')
    for num in range(num_columns): #Runs through the columns
        if num < 10:
            print(num, end = '  ') #Prints puzzle spacing and numbers
        else:
            print(num, end = ' ')
    print('')


    # ADD code to print each row number and row.

    lines = puz.split("\n") #splits puzzle
    for i in range(len(lines)): #runs through puzzle lines
        if i < 10: #Continues to run until there are 10 columns
            print(i,  end = '   ')
        lines[i]=lines[i].strip()
        for character in lines[i]: #runs through and svtrips the characters
            character = character.strip()
            print(character, end = "  ")
        print('')

            

def print_words(alist):
    """ (list of str) -> NoneType

    Print the word from alist.
    """
    remaining_words = "The remaining words to be found: "
    print(remaining_words, end = '') 

    for item in alist: #runs through remaining words in the list
        print(item, end = ' ')
    print('')


def game_over(words):
    """ (list of str) -> bool

    Return True if words is empty.

    >>> game_over(['dan', 'paul'])
    False
    >>> game_over([])
    True
    """
    if len(words) == 0: #ends game if words is 0
        return False
    else:
        return True
##    return (len(words) < 1)

#Independent Function Tests
##print(game_over([]))


def get_direction_calculate_score(puz, guess, current_player_name, words):
    """ (str, str, str, str, list of str) -> int

    Prompt for the direction and the row or column number.  Based on these
    answers and the number of words left to be found, calculate and return the
    appropriate score.
    """
    score1 = 0 #set score 1 value
    score2 = 0 #set score 2 value
    direction_list = ["up", "down", "forward", "backward"] #set directions
    
    direction = input("What direction? ") #ask user for direction
    direction = direction.lower() #make direction lowercase
    
    while direction not in direction_list: #continues to ask for direction until user chooses a correct direction
        direction = input("What direction? ")
    direction = direction.lower()

    direction_factor = get_factor(direction) #runs direction program


    if direction == "up" or direction == "down": #asks user for column if vertical
        num = int(input("What Column? "))

    else: #asks user for row if horizontal
        num = int(input("What row? "))


    current_player = get_current_player(current_player_name) #gets player

    if check_guess(guess, puz, direction, words, num) and guess in words: #checks the user guess
        if len(words) >= 5:
            direction_factor = direction_factor *5
        elif len(words) == 1: #adds points accordingly for how many words he/she gets right
            direction_factor = (direction_factor * 9) + 25
        elif len(words) < 5:
            direction_factor = (10 - len(words)) * direction_factor

        if current_player == "Player One":
            score1 += direction_factor #adds the points to the player
            return score1
        else:
            score2 += direction_factor #adds score for other player
        return score2
    else:
        return 0

    
def check_guess(guess, puz, direction, words, num): #Checks the user inputted guess
    if direction == "forward": #runs if forward
        if contains(get_row(puz, num), guess): 
            return True
    elif direction == "backward": #runs if backward
        if contains(reverse(get_row(puz, num)), guess):
            return True
    elif direction == "up": #runs if up
        if contains(reverse(get_column(puz, num)), guess):
            return True
    elif direction == "down": #runs if down
        if contains(get_column(puz, num), guess):
            return True
    return False

def get_factor(direction):
    ''' (str) -> int
    '''
    if direction == "forward":
        return FORWARD_FACTOR
    
    elif direction == "down":
        return DOWN_FACTOR
    
    elif direction == "backward":
        return BACKWARD_FACTOR
    
    else:
        return UP_FACTOR
    
def take_turn(puz, words, current_player_name):
    """ (str, list of str, str) -> int

    Prompt the current player (according to player_one_turn) to  guess a word
    Call `get_direction_calculate_score` to do its work, which returns a scoce
    Remove the guess from the list of words.
    Return the score
    """


    # Prompt for a word from the list of valid words.  
    guess = input(current_player_name + ', please enter a word: ').strip() #prompts user for word

    score = get_direction_calculate_score(
        puz, guess, current_player_name, words)

    # Remove the guess from the word list.
    if score > 0:
        words.remove(guess)

    return score #returns thd score


def play_game(puz, words):
    """ (str, list of words) -> Nonetype

    Prompt the players to guess words that occur in the puzzle.
    Print the score after each turn.  Print the winner.
    """

    # Whether it's Player One's turn; if False, it's Player Two's turn.
    player1_turn = True

    # The scores for the two players.


    print('''***************************************
**       Where's That Word?          **
***************************************''')
    player1_score = 0
    player2_score = 0

    
    while game_over(words):
        print_puzzle(puz) #prints the puzzle and words guessed
        print_words(words)
        
        if player1_turn:
            score = take_turn(puz,words,'Player One') #runs through first players turn
            player1_score += score
            player1_turn = False
            print('Player 1 score =',player1_score)
            
        else:
            score2 = take_turn(puz,words,'Player Two') #runs through second players turn
            player2_score += score2
            player1_turn = True
            print('Player 2 score =',player2_score)

            
    if player1_score > player2_score: #decides who wins between the two players
        print("Winner is Player 1")
    elif player1_score == player2_score:
        print("Tie game!")
    else:
        print("Winner is Player 2")

def main(): #holds the puzzle
    puzzle = """rmhlzxceuq 
    bxmichelle
    mnnejluapv
    caellehcim
    xdydanagbz
    xiniarbprr
    vctzevbkiz
    jgfavqwjan
    quotjenhna
    iumxddbxnd
    """     # once static program is working
            # to be changed to read from a file n/grid.txt

    words = ['brian', 'dan', 'jen', 'michelle', 'paul']  # same as above
            # to be changed to read from a file n/word.txt
                   
    
    play_game(puzzle, words)
    
main()
