# ----------------------------------------------------------
# --------    HW 4: Reverse Guessing Game          ---------
# ----------------------------------------------------------

# ----------------------------------------------------------
# Please answer these questions after having completed this
# program
# ----------------------------------------------------------
# Name:
# Hours spent on program 2:
# Collaborators and sources:
#   (List any collaborators or sources here.)
# ----------------------------------------------------------


# Write your two functions for the reverse guessing game here
# of course, if it helps to have more functions, do that!

def feedback():
    prompt = input('Is this (c)orrect, (h)igh, or (l)ow:')
    prompt = str.lower(prompt)
    
    while prompt[0] not in ('c','h','l'):
        print ("I'm sorry, I didn't understand that.")
        prompt = input('Is this (c)orrect, (h)igh, or (l)ow:')

    return prompt[0]

def play_game():
    guess_num = 50
    low = 1
    high = 100
    pos_range = [1,101]
    first_guess = (pos_range[0]+pos_range[1]) // 2
    
    print("Think of a number between 1 and 100 and I will guess it.  Press return to start.")
    print('I guess', str(guess_num) + '.')
    theprompt = feedback()
    total = 1
    
    while theprompt != 'c':

        if theprompt == 'l':
            pos_range[0] = first_guess
            first_guess = (pos_range[0] + pos_range[1])//2
            total += 1
            print('I guess', str(first_guess) + '.')
            theprompt = feedback()

        if theprompt == 'h':
            pos_range[1] = first_guess
            first_guess = (pos_range[0] + pos_range[1])//2
            total += 1
            print('I guess', str(first_guess) + '.')
            theprompt = feedback()

    if theprompt == 'c':
        print ("I won in", total, "guesses!")
   
    
    
