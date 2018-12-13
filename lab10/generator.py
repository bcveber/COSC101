#Brian Veber, Lab 10

import random

def noun_phrase():
    '''
    () --> (str)
    Takes an random article from a list and a random noun from a list
    and adds them together.
    
    >>> noun_phrase()
    LOVE AN
    >>> noun_phrase()
    WORLD THE
    '''
    
    
    noun = (random.choice(open('nouns.txt').readline().split()))
    article = (random.choice(open('articles.txt').readline().split()))

    noun_phrase = article + ' ' + noun

    return(noun_phrase)

def prepositional_phrase():
    '''
    () --> (str)
    Takes a random preposition from a list and runs noun_phrase() to get
    a random noun_phrase and adds them together.
    >>> prepositional_phrase()
    PAST LITERATURE AN
    '''
    
    nounphrase = noun_phrase()
    #print(nounphrase)
    preposition =(random.choice(open('prepositions.txt').readline().split()))

    prepositional_phrase = preposition + ' ' + nounphrase

    return prepositional_phrase

def verb_phrase():
    '''
    () --> (str)
    Takes a random verb from a list, a random noun phrase from noun_phrase
    fuunction, and a random prepositional phrase from prepositional_phrase function.
    >>> verb_phrase()
    ABILITY THE
    ABOUT COMPUTER AN
    'JUMP ABILITY THE ABOUT COMPUTER AN'
    '''
    
    nounphrase = noun_phrase()
    #print(nounphrase)
    
    prepositionalphrase = prepositional_phrase()
    #print(prepositionalphrase)
    
    verb = (random.choice(open('verbs.txt').readline().split()))

    verb_phrase = verb + ' ' + nounphrase + ' ' + prepositionalphrase

    return verb_phrase

def sentence():
    '''
    () --> (str)
    Takes a random noun phrase and a random verb phrase and adds them together. 
    
    >>> sentence()
    THANKS AN TALK MUSIC A ON LOVE A
    '''
    verbphrase = verb_phrase()
    nounphrase = noun_phrase()

    sentence = nounphrase + ' ' + verbphrase

    return sentence

def generator():
    '''
    () ---> (str)
    Generates a list of sentences based on how many sentences the user requests using
    the sentence() function.
    
    >>> generator()
    Enter the number of sentences: 4
    ABILITY AN ADD METHOD AN ONTO MUSIC AN
    LAW A VISIT HEALTH AN MINUS HISTORY AN
    FOOD A JUMP DATA THE BUT HISTORY A
    FAMILY AN PASS WORLD A DESPITE SOFTWARE A
    >>>
    '''
    sentence_list = []
    sentences = int(input ('Enter the number of sentences: '))

    for amount in range (sentences):
        sentence_list += [(sentence())]

    return sentence_list

def main():
    '''
    () ---> (str)
    Displays a set of sentences user the generator() program.
    >>> main()
    Enter the number of sentences: 4
    FOOD A OBEY HEALTH THE MINUS DATA AN
    BIRD AN WALK BIRD THE AT COMPUTER AN
    DATA A JUMP LAW A AT THEORY AN
    LITERATURE THE JUMP MAP THE EXCEPT PERSON AN
    '''
    sentences = generator()
    for item in sentences:
        print(item)
                          


        
        
