#Brian Veber, Lab 06

def find (s, substring, start, end):
    '''
    (str,str,int,int) --> (int)
    This function returns the index of the first occurence of the string substring
    within s, or the
    value -1 if substring isn't found.
    '''
    newstring = s[start:end]
    x = -1
    found_substring = False
    for index in range(len(newstring)):
        substring_slice = newstring[index: len(substring)+index]
        if substring_slice == substring:
            found_substring = True
            break
    if found_substring == True:
        return index+start
    if found_substring == False:
        return x
        
#x=find('blahblah', 'ah', 0, 8)
#print (x)

def multiFind (someString, substring, start, end):
    '''
    (str,str,str,str) ---> [int,int]
    Returns a list that contains zero or more indexes at which the string
    substring occurs within the string someString.
    "'ACTTGCTG', 'CT', 0, 7" ---> [1,5]
    '''
    newstring = someString[start:end]
    x = -1
    found_substring = False
    found_substring2 = False
    for index in range(len(newstring)):
        substring_slice = newstring[index: len(substring)+index]
        if substring_slice == substring:
            found_substring = True
            break
    for index in range(len(newstring)):
        if found_substring == True:
            substring_sli2ce2 = newstring[index+start: len(substring)+index+start]
            if substring_slice2 == substring:
                found_substring2 = True
                break
        if found_substring == True and foundsubstring_2 == True:
            return (index+start, index+start+start)

#x=multiFind('ACTTGCTG', 'CT', 0, 7)
#print (x)


def normalize_word (word):
    '''
    (string) ---> (string)
    accepts a string as a parameter and returns a normalized string in which all
    non-alphanumeric characters are removed, and all remaining letters are
    lower-cased.
    "Aren't" ----> "arent"
    '''
    word_edit = ''
    for individual_letter in word:
        if individual_letter.isalpha() == True:
            individual_letter = individual_letter.lower()
            word_edit += individual_letter
        elif individual_letter.isdigit() == True:
            word_edit += individual_letter
        
    return word_edit
    
y = normalize_word("Aren't")
print(y)

        
def normalize_sentence (sentence):
    '''
    (string) ---> (string)
    accepts a string as a parameter and returns a normalized string in which
    all words are normalized, and in which there is only a single space between
    words (and no spaces at the beginning or end of the string).
    "This isn't a sentence!!!!" ---> "this isnt a sentence"
    '''

    word_edit = ''
    for individual_letter in sentence:
        if individual_letter.isalpha() == True:
            individual_letter = individual_letter.lower()
            word_edit += individual_letter + ' '
            word_edit.strip()
        elif individual_letter.isdigit() == True:
            word_edit += individual_letter + ' '
            word_edit.strip()
        
    return word_edit

a = normalize_sentence("This isn't a sentence!!!")
print(a)

def count_letters(word):
    '''
    (string) ---> (string)
    accepts a string as a parameter, and returns a list of integers of length
    26, containing counts of each letter of the string. Words such as A and a
    are not treated the same. No symbols or numbers.
    "ABCDE" ---> "1111100000000000000000000"
    '''
    index_list = ord('A')
    word_list = ''
    while index_list < ord('Z'):
        total = 0
        for individual_letter in word:
            if chr(index_list) == individual_letter or chr(index_list).lower() == individual_letter:
                total = total + 1
        word_list = word_list + str(total)
        index_list = index_list + 1
    return word_list
    

c = count_letters("ABCDE")
print(c)

def names_between(roster, name1, name2):
    '''
    Takes a list of strings representing people and two individual names. The functions constructs and returns
    a new list that contains only the list of names between and including the two names passed in as parameters.
    roster = ['cucura', 'fourquet', 'vijay', 'lyboult', 'smith'] ---> 'fourquet', 'vijay', 'lyboult'
    '''
    roster_index = 0
    shorter_list = str(0)

    while roster_index < len(roster):
        if roster[roster_index] == name1:
            roster_index = roster_index
        roster_index = roster_index + 1
    shorter_list = roster[start_point: name1+name2]
    x = shorter_list
    print(x)
        
roster = ['cucura', 'fourquet', 'vijay', 'lyboult', 'smith']
shorter_list = names_between(roster, 'fourquet', 'lyboult')

def roster_section(roster, start_point, lng):
    '''
    (str, int, int) ---> (str(x) - depending on int values)
    Asks for a roster and returns selected subsections of that roster at a time. Accepts a list of strings
    and two integers.
    roster = ['cucura', 'fourquet', 'vijay', 'lyboult', 'smith'] ---> 'lyboult' 'smith'
    '''
    
    roster_index = 0
    shorter_list = str(0)

    while roster_index < len(roster):
        if roster[roster_index] == start_point:
            roster_index = roster_index
        roster_index = roster_index + 1
    shorter_list = roster[start_point: start_point+lng]
    x = shorter_list
    print(x)
        
roster = ['cucura', 'fourquet', 'vijay', 'lyboult', 'smith']
shorter_list = roster_section(roster, 3, 2)
