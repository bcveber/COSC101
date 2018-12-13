#Brian Veber, Lab04, char.py

#6a

def doublechar(astring):
    '''
    (str) --> str
    Prints double the characters for each character given.
    '''
    acum=""
    for letter in astring:
        acum = acum +(letter*2)
    return acum

print(doublechar('hey'))

#6b

def substring_count (s, substr):
    '''
(str, str) --- > int
    Takes letters in cat/dog with some capitalized and some not and returns a
    number between 0-2.
    '''
    count = 0
    for idx in range (len(s)-2):
        if substr[0] == s[idx] and substr[1]==s[idx+1]:
            count+=1
    return count

cat = substring_count ("CATtac", "cat")
print (cat)

#6c

def catdog(s):
    '''
    (str) ---> boolean
    This program returns true or false based off of cat and dog appearances.
    >>>print(catdog('catdogeeecat'))
    False
    >>>print(catdog('catdog')
    True
    '''
    dog = 'dog'
    cat = 'cat'
    cat_number = 0
    dog_number = 0

    for idx in range(len(s)-2):
        if cat[0] == s[idx] and cat[1] == s[idx+1] and cat[2] == s[idx+2]:
            cat_number += 1
        elif dog[0] == s[idx] and dog [1] == s[idx+1] and dog[2] == s[idx+2]:
            dog_number += 1
    if cat_number == dog_number:
        return True
    else:
        return False

print(catdog('catdogeeecat'))
