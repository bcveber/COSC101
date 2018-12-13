# The constants describing the multiplicative factor for finding a word in
# a particular direction.  These should be used in function get_factor.
FORWARD_FACTOR = 1
DOWN_FACTOR = 2
BACKWARD_FACTOR = 3
UP_FACTOR = 4

def get_current_player(player_one_turn):
    """ (bool) -> str

    Return 'Player One' if player_one_turn is True; otherwise, return
    'Player Two'.

    >>> get_current_player(True)
    'Player One'
    >>> get_current_player(False)
    'Player Two'
    """

    if player_one_turn == True:
        return "Player One"
    else:
        return "Player Two"
    
#Independent Function Test    
#print(get_current_player(True))

# Helper functions.  Do not modify these, although you are welcome to call
# them.

def get_row(puz, row_num):
    """ (str, int) -> str

    Precondition: 0 <= row_num < number of rows in puzzle

    Return row row_num of puzzle.

    >>> get_row('abcd\nefgh\nijkl\n', 1)
    'efgh'
    """

    separated_words = puz.split("\n")
    final_word = separated_words[row_num]

    return final_word

#Independent Function Test
#print("get_row Function Test")
#print(get_row('abcd\nefgh\nijkl\n', 1))

def get_column(puz, col_num):
    """ (str, int) -> str

    Precondition: 0 <= col_num < number of columns in puzzle

    Return column col_num of puzzle.
    >>> get_column('abcde\nefghi\nijklm\n', 1)
    'bfj'
    """
    separated_words = puz.split("\n")
    final_list = ''
    for word in range(len(separated_words) - 1 ):
        character = separated_words[word].strip()
        final_list += character[col_num]

    return final_list

        
#Independent Function Test
#print("get_column Function Test")
#print(get_column('abcd\nefgh\nijkl\n', 1))   


def reverse(s):
    """ (str) -> str

    Return a reversed copy of s.

    >>> reverse('abc')
    'cba'
    """
    if s == "":
        return s
    else:
        return reverse(s[1:]) + s[0]
    
#Independent Function Test
#print("Reverse Function Test")
#print(reverse("abc"))

def contains(s1, s2):
    """ (str, str) -> bool

    Return True iff s2 appears anywhere in s1.

    >>> contains('abc', 'bc')
    True
    >>> contains('abc', 'cb')
    False
    """
    
    if s1 == '':
        return False
    
    if len(s2) > len(s1):
        return False
    
    if s1[:len(s2)] == s2:
        return True
    
    change = s1[1:]
    
    return contains(change, s2)

