#Brian Veber, HW_06

#Sources:
    #1. Ben Lerner for how to end the game: http://stackoverflow.com/questions/17180795/how-do-you-end-a-python-guess-number-game

import random
import sys #for ending the game with '0'

def get_randomcolorlist():
    '''
    () ---> (list)
    ---
    Introduces the user to the game and gives instructions and list of available colors.
    Takes a random list of C colors, and then creates a new color list with the
    requested code length L via randomization and while loops. Handles exceptions (user not entering color properly) and gives the option to exit.
    ---
    >>> get_randomcolorlist()
    Welcome to the color guessing game! Type "0" to end the game at any time.
    Here is how the game works: You will be prompted to create a certain length of code with a certain number of colors. Then, you will attempt to guess the code. For each guess, you will get a group of white pegs and black pegs. If you get a black peg, that means that you have correctly guessed both the color and the position of the color in the code. If you get a white peg, that means that you have correctly guessed a color in the code, but you did not guess the correct position. If the color is not in the code, then you will receive no peg. You will only have 12 guesses, so use them wisely. Good luck!
    What length of code do you want? 3
    How many colors do you want? 4
    Your requested amount of colors cannot exceed the desired code length. Please try again.
    What length of code do you want?
    ---
    >>> get_randomcolorlist()
    Welcome to the color guessing game! Type "0" to end the game at any time.
    Here is how the game works: You will be prompted to create a certain length of code with a certain number of colors. Then, you will attempt to guess the code. For each guess, you will get a group of white pegs and black pegs. If you get a black peg, that means that you have correctly guessed both the color and the position of the color in the code. If you get a white peg, that means that you have correctly guessed a color in the code, but you did not guess the correct position. If the color is not in the code, then you will receive no peg. You will only have 12 guesses, so use them wisely. Good luck!
    What length of code do you want? 4
    How many colors do you want? 3
    These are the colors you have to choose from: ['blue', 'green', 'red', 'white', 'black', 'yellow', 'grey', 'orange', 'purple', 'pink']
    When entering your guess, enter the color followed by a comma and a space except for the last color. For example, "red, green, blue"
    ['blue', 'yellow', 'blue', 'yellow']
    
    '''
    random_colorlist = [] #Original color list
    final_rlist = [] #List with requested colors
    lower_color = ''
    switch = True
    
    print ('Welcome to the color guessing game! Type "0" to end the game at any time.')
    print ('Here is how the game works: You will be prompted to create a certain length of code with a certain number of colors. Then, you will attempt to guess the code. For each guess, you will get a group of white pegs and black pegs. If you get a black peg, that means that you have correctly guessed both the color and the position of the color in the code. If you get a white peg, that means that you have correctly guessed a color in the code, but you did not guess the correct position. If the color is not in the code, then you will receive no peg. You will only have 12 guesses, so use them wisely. Good luck!') 
        
    while switch == True: #Keep running through until user enters valid set of L and C
        try:
            L = int(input ('What length of code do you want? '))
            if L == 0:  #Exit if user enters 0
                print ('Thank you for playing!')
                sys.exit(0)
            C = int(input ('How many colors do you want? '))
            if C == 0:
                print ('Thank you for playing!')
                sys.exit(0)
        except ValueError: #Asks the user to re-enter if user enters invalid combination
            print ('Please try again and enter numbers only in numerical form.')
        if L >= 1: #L and C must be greater than 0 and must be numerical, otherwise program will prompt user again
            if C >= 1:
                if L >= C: #The code must be greater than the number of colors requested
                    switch = False
                else:
                    print ('Your requested amount of colors cannot exceed the desired code length. Please try again below.')

    available_colors = ['blue', 'green', 'red', 'white', 'black', 'yellow', 'grey', 'orange', 'purple', 'pink'] #Tells user available colors to choose from when guessing

    print('These are the colors you have to choose from:', available_colors)
    print('When entering your guess, enter the color followed by a comma and a space except for the last color. For example, "red, green, blue"') #Explains to user how to guess

    while len(random_colorlist) < C: #Creates a random set of the requested number of colors
        rcolor = random.choice(available_colors)
        random_colorlist += [rcolor]
    #print (random_colorlist) --- #testing variable

    while len(final_rlist) < L: #Takes the random set of colors to create a code set
        rcolor = random.choice(random_colorlist)
        final_rlist += [rcolor]
    #print (final_rlist) --- #testing variable

    return final_rlist #Returns the code to guess

def code_guess():
    '''
    () ---> (list)
    ---
    Prompts the user to guess the code and returns the guessed colors in a list. Handles errors.
    ---
    >>> code_guess()
    Guess the code: red, green, blue
    ['red', 'green', 'blue']
    '''
    guess_set = '' #Appropriate variable name

    try: #Use try to handle errors
        guess_set = input('Guess the code: ')
        if str(0) in guess_set:
            print ('Thank you for playing!') #Ends game if user enters 0
            sys.exit(0)
    except ValueError: #Handles error of user not entering colors properly
       print ('Invalid input. Remember, enter the color followed by a comma and a space: "red, green, blue"')
       guess_set = input('Guess the code: ')
        
    guess_set = guess_set.lower() #make colors all lowercase so other functions can easily interpret them
    guess_set = guess_set.replace(',', '').split() #make colors into a list without the commas
    
    return guess_set #return user guesses
   
def list_comp_helper(code, guess_list):
    '''
    (list, list) ---> (int)
    ---
    Returns the number and colors of pegs that the user got with their guess. Handles errors.
    Essentially compares the two lists to each other.
    ---
    >>> list_comp_helper(['red', 'blue', 'green'], ['blue', 'red', 'green'])
    You got 1 black peg(s) and 2 white peg(s).
    Using the peg(s) you got, try another guess below.
    1
    ---
    >>> list_comp_helper(['red', 'blue', 'green'], ['blue', 'red', 'green'])
    You got 1 black peg(s) and 2 white peg(s).
    Using the peg(s) you got, try another guess below.
    1
    '''

    peglist = [] #Appropriate variable name
    
    #print(ranger)
    #print (code) #--- Tester functions
    #print (guess_list)
    
    for color in range(len(code)): #Run through all colors in the lists
        try:          
            if guess_list[color] == code[color]: #Returns a black peg if colors match eachother 
                peglist += ['Black Peg']

            if guess_list[color] in code: #Returns a white peg if colors don't match eachother but the guess is within the code
                if guess_list[color] != code[color]:
                    peglist += ['White Peg']

            else:
                peglist += ['No Peg']
                
        except IndexError:
            print ('Invalid input. Remember, enter the color followed by a comma and a space: "red, green, blue"')
            code_guess()

    black_pegs = peglist.count('Black Peg') #Counts number of black pegs in list
    white_pegs = peglist.count('White Peg') #Counts number of white pegs in list

    print ('You got', black_pegs, 'black peg(s) and', white_pegs, 'white peg(s).') #Returns how many black and white pegs user got 

    if int(black_pegs) != int(len(code)): #If the black pegs do not equal the code (which would win the game), the user guesses again
        print ('Using the peg(s) you got, try another guess below.')

    return black_pegs   

def main():
    '''
    () ---> (str)
    ---
    Uses all the functions to run the entire program through. Includes congratulatory or failure notes.
    ---
    >>> main()
    Welcome to the color guessing game! Type "0" to end the game at any time.
    Here is how the game works: You will be prompted to create a certain length of code with a certain number of colors. Then, you will attempt to guess the code. For each guess, you will get a group of white pegs and black pegs. If you get a black peg, that means that you have correctly guessed both the color and the position of the color in the code. If you get a white peg, that means that you have correctly guessed a color in the code, but you did not guess the correct position. If the color is not in the code, then you will receive no peg. You will only have 12 guesses, so use them wisely. Good luck!
    What length of code do you want? 3
    How many colors do you want? 3
    These are the colors you have to choose from: ['blue', 'green', 'red', 'white', 'black', 'yellow', 'grey', 'orange', 'purple', 'pink']
    When entering your guess, enter the color followed by a comma and a space except for the last color. For example, "red, green, blue"
    Guess the code: red, green, blue
    You got 1 black peg(s) and 0 white peg(s).
    Using the peg(s) you got, try another guess below.
    Guess the code: red, red, yellow
    You got 0 black peg(s) and 0 white peg(s).
    Using the peg(s) you got, try another guess below.
    Guess the code: 
    '''
    code =  get_randomcolorlist() #Get code to guess
    guess_set = code_guess() #Get user guess inputs
    black_pegs = list_comp_helper(code, guess_set) #Check how many pegs the user got
    guesses = 1
    
    #print (code)
    #print(black_pegs) --- #tester functions
    #print (len(code))

    while black_pegs != len(code): #Function will run until the user reachs 12 guesses or gets all black pegs
        guess_set = code_guess()
        black_pegs = list_comp_helper(code, guess_set)
        guesses += 1

        if guesses == 12:
            print ('You have used your 12 guesses and have not correctly guessed the code. Sorry, but you have lost the game.') #Code to limit the user to 12 guesses
            print ('The code you were trying to guess was', code, 'have a good day!')
            sys.exit()
    
    if int(black_pegs) == int(len(code)): #If the user gets all black pegs, they win the game
        print ('Congratulations. You won the game and successfully guessed the code!')
        print ('You took a total of', guesses, 'guesses. Great job!')

    #print (black_pegs)
    #print (white_pegs) ---- #tester functions
    #white_pegs = count. ('White Peg')
