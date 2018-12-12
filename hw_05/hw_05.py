#Brian Veber, hw_05 FINAL
#Collaborators: Tutors, Shamarcus Doty, Matthew Copeland
#Hours Spent: No joke, atleast 25 hours. 
#Sources:
    #1) Runestone interactive 'How To Think Like A Computer Scientist.'
    #2) Jim Clifford and Miriam Posner for the Counter() function and the most_common() function. http://programminghistorian.org/lessons/counting-frequencies
    #3) Doug Hellmann for more info on Counter() https://pymotw.com/2/collections/counter.html
    #4) User 'katriealex' for how to reverse a list - http://stackoverflow.com/questions/13530798/python-reverse-order-of-list
    #5) User 'Ashwini Chaudhary' for how to use itertools to get a set of pairs - http://stackoverflow.com/questions/18201690/get-unique-combinations-of-elements-from-a-python-list
    #6) User 'Louis93' for how to remove things from a Counter() set - http://stackoverflow.com/questions/7154312/how-do-i-remove-entries-within-a-counter-object-with-a-loop-without-invoking-a-r
    #7) User 'Daniel Stutzbach' for how to remove numbers from a list - http://stackoverflow.com/questions/3159155/how-to-remove-all-integer-values-from-a-list-in-python

from collections import Counter     #Import Counter program
import itertools    #Import itertools

def word_frequencies(filename, wordlist):
    '''
    Takes two parameters: a file and a list of words. The program opens the file
    and reads the lines of the file. Then it runs a for loop searching for the words
    within the wordlist, by breaking down the lines of the file and then the words
    of a file with other for loops. Once it is down to the individual word, if the word
    is a match then it will add to the word count.
    ----
    word_frequencies('test.txt', ['list', 'of', 'Australia', 'a'])
    [3, 4, 0, 3]
    word_frequencies('hw3.txt', ['a', 'the', 'lab'])
    [15, 75, 0]
    ----
    Testing: Tried all homework files. Used the search feature in txt files to make
    sure that my number matched them.
    '''
    count = 0   #This will count how many times the words show up
    file = open(filename)   #Opens said file
    wholefile = file.readlines()    #Reads the entire file
    word_frequencies = []   #List to store word frequencies
    for chosen_word in wordlist:    #Runs through chosen words from wordlist
        for line in wholefile:  #Breaks the file down line by line
            for word in line.split():   #Breaks the file down word by word
                word = word.lower().strip(""" \n\t,./<>?;':"[]\{}|-=`1~!@#$%^&*()_+""")     #Strips word to the raw letters so it can be interpreted properly
                if chosen_word == word:
                    count += 1  #Adds the word to count if it is a match
                    
        word_frequencies += [count]     #Displays the count for that individual word here
        count = 0   #Reset so it does not interfere with any other words  
    return (word_frequencies) #Returns the final list

def compare_files(filename1, filename2, wordlist):
    '''
    Compares the word frequencies of two files with a given wordlist. Subtracts
    the two values from eachother and takes the absolute value, then makes a new
    list with the updated set of numbers.
    ----
    compare_files('hw1.txt', 'hw2.txt', ['list', 'of', 'Australia', 'a'])
    [0, 35, 0, 34]
    compare_files('hw2.txt', 'hw3.txt', ['list', 'of', 'lab', 'a'])
    [3, 21, 0, 14]
    ----
    Testing: Made sure 0 cases did not return an error, made sure no negative values
    were present. Compared multiple files with different words, as shown above.
    '''
    difference_list = [] #This will be the new list
    file_1_list = word_frequencies(filename1, wordlist)     #Get word frequencies for first file
    file_2_list = word_frequencies(filename2, wordlist)     #Get word frequencies for second file
    for counts in range (len(file_1_list)):     #Run through each wordcount, will end once it has ran through all word counts
        new_subtracted_list_values = abs(file_1_list[counts] - file_2_list[counts])  #Subtracts the two values and makes sure they are positive
        difference_list += [new_subtracted_list_values]   #Adds that individual word frequency to a new frequency set
    return (difference_list)

def file_common_words(filename, x):
    '''
    This function takes a file and the number of x words that occur most frequently
    within the file. The function reads the lines of the file, then runs a for
    statement with the lines and then the words of the file, stripping the words
    appropriately. It then makes a new list with all of these words, and then the
    Counter function is used to count how many word occurences happen in the file.
    Once this has been done, the most_common() function within Counter is used
    to make counted_words into a dictionary. Now that the file is a dictionary,
    the sorted function can run which is done in reverse due to alphabetical requirements.
    The function is then turned back into a Counter set, and most_common is ran
    again and creates a new list with only the words within the list.
    ----
    Testing: Used command+F search function within text file to make sure Counter
    function counted correctly, also compared the list using the word_frequencies
    program I wrote above. I also used print(counted words) to make sure that the
    words from the counter 1) transferred into the list properly and 2) were done so
    in reverse alphabetical order. In 'hw3.txt', I also added 'of of of of of of of
    is is is is is is is is is' to make 'of' 'is' and 'and' all 28, so then I could
    make sure that the words sorted reverse alphabetically properly.
    ----
    file_common_words('hw3.txt', 3)
    (Print test to compare with below) ---> Counter({'the': 66, 'to': 31, 'of': 28, 'is': 28, 'and': 28, '': 24, 'will': 17, 'file': 15, 'a': 15, 'image': 14, 'your': 13, 'you': 13, 'that': 13, 'for': 13, 'blue': 13, 'are': 13, 'red': 11, 'value': 10, 'this': 10, 'on': 10, 'function': 10, '70': 10, 'point': 9, 'green': 9, 'The': 9, '0': 9, 'in': 8, 'each': 8, 'assignment': 8, 'an': 8, 'with': 7, 'values': 7, 'it': 6, 'functions': 6, 'color': 6, 'code': 6, 'below': 6, 'Functions': 6, '2': 6, 'write': 5, 'take': 5, 'so': 5, 'run': 5, 'points': 5, 'hw_03.py': 5, 'files': 5, 'channel': 5, 'by': 5, 'any': 5, 'You': 5, 'This': 5, 'Image': 5, '255': 5, 'sure': 4, 'side': 4, 'same': 4, 'provided': 4, 'pixel': 4, 'other': 4, 'not': 4, 'negative': 4, 'images': 4, 'grayscale': 4, 'brightness': 4, 'be': 4, 'autograder': 4, 'Grayscale': 4, '3': 4, 'transformation': 3, 'save_image': 3, 'save': 3, 'pres_casey.gif': 3, 'original': 3, 'or': 3, 'object': 3, 'names': 3, 'multiple': 3, 'may': 3, 'list': 3, 'have': 3, 'down': 3, 'colgate1.gif': 3, 'between': 3, 'before': 3, 'becomes': 3, 'as': 3, 'additional': 3, 'We': 3, 'Points': 3, 'Note': 3, 'March': 3, 'In': 3, 'However': 3, '6': 3, 'yellow': 2, 'worth': 2, 'work': 2, 'vertical_flip': 2, 'uses': 2, 'use': 2, 'updated': 2, 'two': 2, 'than': 2, 'testing': 2, 'test': 2, 'submitting': 2, 'start': 2, 'should': 2, 'set': 2, 'scroll': 2, 'save_images': 2, 'required': 2, 'representing': 2, 're-submit': 2, 'range': 2, 'posterize': 2, 'parameters': 2, 'parameter': 2, 'over': 2, 'only': 2, 'one': 2, 'number': 2, 'need': 2, 'name': 2, 'manipulation': 2, 'loops': 2, 'light': 2, 'left': 2, 'integer': 2, 'increase_contrast': 2, 'inclusive': 2, 'if': 2, 'horizontal_mirror': 2, 'homework': 2, 'gradescope': 2, 'go': 2, 'from': 2, 'four': 2, 'end': 2, 'download': 2, 'directory': 2, 'diff': 2, 'dark': 2, 'cycle_colors': 2, 'copy': 2, 'comments': 2, 'colgate3.gif': 2, 'colgate2.gif': 2, 'check': 2, 'cImage.py': 2, "brightness('pres_casey.gif": 2, "brightness('colgate3.gif": 2, "brightness('colgate2.gif": 2, "brightness('colgate1.gif": 2, 'because': 2, 'auto-graded': 2, 'attempt': 2, 'at': 2, 'around': 2, 'all': 2, 'able': 2, 'Use': 2, 'Result': 2, 'Manipulation': 2, 'Gradescope': 2, 'For': 2, 'Be': 2, '5pm': 2, '32': 2, '28': 2, '22': 2, 'wrap': 1, 'without': 1, 'which': 1, 'where': 1, 'what': 1, 'was': 1, 'visit': 1, 'vice': 1, 'vertically': 1, "vertical_flip('pres_casey.gif": 1, "vertical_flip('colgate3.gif": 1, "vertical_flip('colgate2.gif": 1, "vertical_flip('colgate1.gif": 1, 'version': 1, 'versa': 1, 'useful': 1, 'used': 1, 'until': 1, 'understand': 1, 'unchanged': 1, 'total': 1, 'top': 1, 'times': 1, 'through': 1, 'these': 1, 'there': 1, 'then': 1, 'textbook': 1, 'tasks': 1, 'successfully': 1, 'strongly': 1, 'strings': 1, 'string': 1, 'statements': 1, 'starter': 1, 'solution': 1, 'smallest': 1, 'small': 1, 'slower': 1, 'shifted': 1, 'series': 1, 'see': 1, 'sections': 1, 'second': 1, "scroll('pres_casey.gif": 1, "scroll('colgate3.gif": 1, "scroll('colgate2.gif": 1, "scroll('colgate1.gif": 1, 'sample': 1, 'rubric': 1, 'round': 1, 'right': 1, 'review': 1, 'return': 1, 'resulting': 1, 'resources': 1, 'reduced': 1, "red_filter('pres_casey.gif": 1, "red_filter('colgate3.gif": 1, "red_filter('colgate2.gif": 1, "red_filter('colgate1.gif": 1, 'red_filter': 1, 'recommend': 1, 'read': 1, 're-run': 1, 'quickly': 1, 'problems': 1, 'problem': 1, 'previous': 1, 'practice': 1, 'posterized': 1, "posterize('pres_casey.gif": 1, "posterize('colgate3.gif": 1, "posterize('colgate2.gif": 1, "posterize('colgate1.gif": 1, 'positive': 1, 'pixels': 1, 'pixel-by-pixel': 1, "pixel's": 1, 'perform': 1, 'own': 1, 'others': 1, 'opened': 1, 'omabafy': 1, 'off': 1, 'occurring': 1, 'objects': 1, "obamafy('pres_casey.gif": 1, "obamafy('colgate3.gif": 1, "obamafy('colgate2.gif": 1, "obamafy('colgate1.gif": 1, 'obamafy': 1, 'numbers': 1, 'notes': 1, 'no': 1, 'nested': 1, "negative('pres_casey.gif": 1, "negative('colgate3.gif": 1, "negative('colgate2.gif": 1, "negative('colgate1.gif": 1, 'nearest': 1, 'must': 1, 'multiples': 1, 'much': 1, 'moves': 1, 'more': 1, 'modify': 1, 'mirrored': 1, 'meaningful': 1, 'max': 1, 'manipulations': 1, 'manipulated': 1, 'manipulate': 1, 'make': 1, 'lists': 1, 'later': 1, 'involves': 1, 'inverting': 1, 'increasing': 1, 'increased': 1, "increase_contrast('pres_casey.gif": 1, "increase_contrast('colgate3.gif": 1, "increase_contrast('colgate2.gif": 1, "increase_contrast('colgate1.gif": 1, 'includes': 1, 'include': 1, 'hw_03.zip': 1, 'horizontally': 1, "horizontal_mirror('pres_casey.gif": 1, "horizontal_mirror('colgate3.gif": 1, "horizontal_mirror('colgate2.gif": 1, "horizontal_mirror('colgate1.gif": 1, 'highly': 1, 'helpful': 1, 'helper': 1, "grayscale('pres_casey.gif": 1, "grayscale('colgate3.gif": 1, "grayscale('colgate2.gif": 1, "grayscale('colgate1.gif": 1, 'gray': 1, 'graded': 1, 'grade': 1, 'going': 1, 'goal': 1, 'get': 1, 'following': 1, 'flipped': 1, 'first': 1, 'find': 1, 'faster': 1, 'fall': 1, 'extract': 1, 'examples': 1, 'example': 1, 'entered': 1, 'encourage': 1, 'edge': 1, 'drastically': 1, 'downloaded': 1, 'doubled': 1, 'docstrings': 1, 'do': 1, 'display': 1, 'digital': 1, 'difficult': 1, 'difference': 1, 'descriptive': 1, 'descriptions': 1, 'described': 1, 'demo': 1, 'decreased': 1, 'deadline': 1, "cycle_colors('pres_casey.gif": 1, "cycle_colors('colgate3.gif": 1, "cycle_colors('colgate2.gif": 1, "cycle_colors('colgate1.gif": 1, 'created': 1, 'create': 1, 'corresponding': 1, 'convert': 1, 'contrast': 1, 'content': 1, 'contain': 1, 'conditional': 1, 'completed': 1, 'complete': 1, 'colors': 1, 'carefully': 1, 'can': 1, 'cImage': 1, 'bottom': 1, 'being': 1, 'begin': 1, 'been': 1, 'based': 1, 'average': 1, 'assingment': 1, 'assignments': 1, 'assigned': 1, 'amount': 1, 'also': 1, 'allowing': 1, 'according': 1, 'above': 1, 'about': 1, 'When': 1, 'Wednesday': 1, 'Variable': 1, 'Typically': 1, 'To': 1, 'Thursday': 1, 'There': 1, 'Submit': 1, 'Submission': 1, 'Style': 1, 'Started': 1, 'So': 1, 'Similarly': 1, 'Shades': 1, 'Python': 1, 'Program': 1, 'Please': 1, 'Pixels': 1, 'Pixel-by-Pixel': 1, 'Page': 1, 'Open': 1, 'Next': 1, 'Mirror': 1, 'Library': 1, 'Instructions': 1, 'If': 1, 'IDLE': 1, 'Homework': 1, 'Grading': 1, 'Getting': 1, 'Friday': 1, 'Flip': 1, 'File': 1, 'Example': 1, 'Do': 1, 'Design': 1, 'Descriptions': 1, 'COSC': 1, 'Below': 1, 'Before': 1, 'Adjust': 1, '9': 1, '8th': 1, '83': 1, '82': 1, '76': 1, '72': 1, '66': 1, '60': 1, '58': 1, '50': 1, '5': 1, '3:00pm': 1, '33': 1, '30': 1, '29': 1, '26': 1, '256': 1, '254': 1, '252': 1, '25': 1, '227': 1, '217': 1, '200': 1, '0th': 1, '0-255': 1})
    ['the', 'to', 'of']
    word_frequencies('hw3.txt', ['the', 'to', 'of'])
    [75, 31, 28]
    file_common_words('hw4.txt', 3)
    ['the', 'of', 'a']    
    '''
    all_words = [] #Initial list assigned a list value
    newlist = [] #Final List assigned a list value

    file = open(filename) 
    file_line = file.readlines()    #File opened and read

    for line in file_line:  #File broken up by lines
        for word in line.split():   #File broken up to individual words
            word = word.lower().strip(""" \n\t,./<>?;':"[]\{}|-=`1~!@#$%^&*()_+""")     #Words stripped
            all_words += [word]     #Stripped words added into a new list
        counted_words = Counter(all_words)  #Counter function ran to turn word set into a Counter
        
    counted_words = counted_words.most_common()     #most_common ran to change it from a Counter function so sorted can run
    counted_words = sorted(counted_words, reverse = True)   #sorted function ran to make reverse alphabetically
    counted_words = Counter(dict(counted_words))    #Counter function ran to change the file from a dictionary so most_common can be used

    #print(counted_words) (I used this print statement to compare with 'newlist').

    remove_word = ['']   #Space removed from Counter set because it is a not a word
    for word in remove_word:
        if word in counted_words:
            del counted_words[word]

    for individual_word, count in counted_words.most_common(x):     #For loop ran with most_common to pick out (x) words
        newlist += [individual_word]    #Individual most common words added into a new list
    return newlist  #Final List returned

def list_common_words(thelist, x):
    '''
    This program is quite similar to file_common_words except it is only dealing with a list of words, not an entire file.
    The program takes a list of words and takes the returns the most frequent/common x words. It starts out by sorting
    the list of given words in reverse alphabetial order, and then the counter function is used to tally the words. After
    this is done, the most_common function is used to return the x list of words that occur most frequently in the file.
    ----
    >>> list_common_words(['b', 'b', 'f', 'f', 'g', 'z', 'g', 'z'], 3)
    ['z', 'g', 'f']
    >>> list_common_words(['b', 'b', 'f', 'f', 'g', 'z', 'a', 'z'], 3)
    ['z', 'f', 'b']
    >>> list_common_words(['b', 'b', 'f', 'f', 'g', 'z', 'a', 'z', 'a'], 3)
    ['z', 'f', 'b']
    >>> list_common_words(['A', 'b', 'd'], 3)
    ['d', 'b', 'a']
    ----
    Testing: For this program, as you can see above, I tested single letters first to make sure they
    were placed in reverse order properly. Then I added more letters such as a, and then added a twice
    to make sure that b was still displayed because it needed to be reverse alphabetical even though
    both a and b appeared two times each. I also used 'print(thelist)' and 'print(word_count)' to make sure
    my program printed and added everything correctly. 
    '''
    
    newlist = []    #Assign variable list name to the to-be final list
    thelist = [y.lower() for y in thelist]  #Make all values in thelist lowercase
    thelist = sorted(thelist, reverse = True)   #Reverse sort to achieve the reverse alphabetical requirement
  #  print(thelist) --(Used this as a test statement to compare to 'word_count')
    
    word_count = Counter(thelist)   #Count the words and turn into a counter function
 #   print(word_count) -- (Used this as a test statement to compare to 'newlist')
    
    for letter,count in word_count.most_common(x):  #Run most_common function to choose most common words
        newlist += [letter]     #Add the most common words to a new word list 'newlist'
        
    return newlist #Returns 'newlist' with the set of x most common/frequent words

def file_list():
    '''
    This program is a helper function which collects a list of files that the user wants to find word
    frequencies from. The function will continue to ask and store file names that the user submits until
    the user enters 'done.'
    ---
    file_list()
    Enter the filename: hw0.txt
    Enter the filename: hw1.txt
    Enter the filename: hw2.txt
    Enter the filename: hw3.txt
    Enter the filename: hello
    Enter the filename: hey
    Enter the filename: done
    ['hw0.txt', 'w1.txt', 'w2.txt', 'w3.txt', 'hello', 'hey']

    >>> file_list()
    Enter the filename: hw00000000000000000000000000000000000000000000000000000000000000000000.txt
    Enter the filename: hw1hw1.txt
    Enter the filename: dfjahslkfh;a
    Enter the filename: done
    ['hw00000000000000000000000000000000000000000000000000000000000000000000.txt', 'hw1hw1.txt', 'dfjahslkfh;a']
   
    ---
    Testing: Testing this file, I noticed that the final filelist included 'done' within the file. So, I
    troubleshooted and was able to remove 'done' from the filelist. For testing I also tried to use multiple file
    names with long strings to make sure the program didn't group or exclude anything.
    '''
    
    filelist = []   #Give a list value to variable that will store all the filenames
    fileresponse = ''   #Give a value to the to-be user responses
    while fileresponse != 'done' and fileresponse != 'DoNe':   #Program will continue to prompt user for filenames until the user enters 'done.'
        fileresponse = input('Enter the filename: ')    #Prompts the user to enter the filename
        filelist += [fileresponse]  #Adds the file the user entered into a list of files

    if 'done' in fileresponse:
        filelist.remove('done')     #Removes 'done' or 'Done' from the filelist because it is not a file
    if 'DoNe' in fileresponse:      #If statement used so error is not produced if 'done' or 'Done' is not in the file
        filelist.remove('DoNe')
        
    return filelist     #Returns the set of files the user entered

def main():
    '''
    This program uses all the helper functions: file_list(), file_loop(filelist),
    two_files(filelist, total_wordset). The function collects a list of files, takes
    the most common words from those files, makes that into a single list, then it
    pairs the files and uses that list to count the word frequencies of the file pairs.
    The file pair with the highest sum is returned with its sum and the file pair
    names themselves.
    ---
    >>> main()
    Enter the filename: hw0.txt
    Enter the filename: hw1.txt
    Enter the filename: hw2.txt
    Enter the filename: hw3.txt
    Enter the filename: hw4.txt
    Enter the filename: syllabus.txt
    Enter the filename: howtostudy.txt
    Enter the filename: done
    How many words would you like to consider: 10
    These are the words that occur most frequently in your files: ['to', 'the', 'and', 'you', 'of', 'is', 'a', 'this', 'program', 'your']
    ('hw1.txt', 'howtostudy.txt') has the highest sum of word occurences with 1076 total occurences.
    ---
    Testing: Much of the testing was done within the helper files, and this main()
    program simply ran all of them together. Though through each step I made sure
    that the addition and the word selections were correct.
    '''
    
    filelist = file_list()  #Runs a loop to gather the file the user wants to check
    total_wordset = file_loop(filelist)     #Counts the most common words, makes a new list with those common words, and takes the common words from that list
    print ('These are the words that occur most frequently in your files:', total_wordset)   #Print the final list to be used later on in the pairs
    select_choice = two_files(filelist, total_wordset)  #Take the pair and its sum
    maxpair_coordinates, maxpair = select_choice    #Appropriate the pair and its sum
    print(maxpair_coordinates, 'has the highest sum of word occurences with', maxpair, 'total occurences.')     #Print the file pair and its sum.

def file_loop(filelist):
    '''
    Picks up from the file_list() function and takes the files through the file_common_words
    function to get the x common words from each file. Then adds all the x common words from each
    file and displays all those values in the one list. It then takes this single list and creates a
    new list with the x number of word frequencies, producing the final list to be ran later. This is done
    by prompting the user for x words, running a for loop to go through the files, and accumulating each x
    words from each file into one large list, and then running list_common_words to get the final list.
    ----
    >>>file_loop(['hw0.txt', 'hw1.txt', 'hw2.txt', 'hw3.txt'])
    How many words would you like to consider: 3
    ['the', 'your', 'you']

    >>>file_loop(['hw0.txt', 'hw4.txt', 'hw3.txt', 'hw2.txt', 'hw1.txt'])
    How many words would you like to consider: 5
    ['to', 'the', 'of', 'your', 'you']
    ----
    Testing: As shown above, I tried multiple file_lists and then I tried multiple word counts, such as 3
    and 5. The function worked properly in that it displayed an error when the file did not exist, letting
    me know that it was accounting for all files. Also down below you can see some of my print statements
    that I used to test it along, making sure that the filelist loop added all of the word frequencies for
    the individual files properly and correctly. 
    '''
    mergedList = []     #Assign list variable to the list that will combine everything
    x = int(input('How many words would you like to consider: '))    #Prompt user for how many words the user would like to consider for each file and the final list
    
    for filename in filelist:   #Run a for loop cycling through the lists the user entered from def file_list()
       single_file_word_set = file_common_words(filename, x)
       #print(eafile)
       mergedList += single_file_word_set   #Add each set of words from individual files into a whole list
    #print (mergedList)
       
    final_list = list_common_words(mergedList, x)   #Takes the new set of words and takes the most common x words to create the final list
    return (final_list)     #Returns the final list with x words

def two_files(filelist, total_wordset):
    '''
    The program is the final helper function that takes the filelist and puts it into pairs. It then
    uses def word_frequencies() to find the sums of each pair of files. The program then runs within the for
    statement an if statement that will take the highest sum and that highest sum will only be replaced if a
    sum that is higher goes through the loop, in which the higher sum will replace the next one. With this,
    the highest sum and the coordinates/pair relating to that sum is displayed.
    ---
    >>> two_files(['hw0.txt', 'hw1.txt', 'hw2.txt', 'hw3.txt', 'hw4.txt', 'syllabus.txt', 'howtostudy.txt'], ['to', 'the', 'and', 'you', 'of', 'is', 'a', 'this', 'program', 'your'])
    (('hw1.txt', 'howtostudy.txt'), 1076)
    ---
    Testing: I made sure the pairs were accurate, non-duplicative and correct with
    the 'print(pairlist)' below. I also went step by step as the pairs were added
    to make sure that they were added properly with print(word_frequencies---) and
    print(sumtotal). I ran through some special cases like 0 with the maxpair to make
    sure that my if statement worked and the proper coordinates were returned.
    '''
    pairlist = list(itertools.combinations(filelist,2))     #Create set of pairs user itertools, 2 is entered to make pairs of 2 (x,y)
    #print(pairlist) --- (Used to test and make sure all pairs were included with the given files)

    maxpair = 0     #Set variable to int value
    maxpair_coordinates = ''    #Set variable to str value
    for (b1, b2) in pairlist:   #Takes pairs from pairlist and runs them through
        #print(word_frequencies(b1, final_list), word_frequencies(b2, final_list)) --- (Used as a test to make sure that the values that added together were correct)
        pair_total = word_frequencies(b1, total_wordset) + word_frequencies(b2, total_wordset)  #Counts the word frequencies of each pair using the wordset from all the files, then adds them together to make the pair into one value
        sumtotal = (sum(pair_total))    #Adds the pair together
        #print(sumtotal) -- (Test - compared with the print statement above to make sure the addition was correct)
        if sumtotal > maxpair:  #Sumtotal will remain the largest sum unless a new set of coordinates comes in and is larger
            maxpair = sumtotal  #If a new pair is larger, sum total will be replaced
            maxpair_coordinates = (b1,b2)   #the pair will not change unless the if statement is activated
    return (maxpair_coordinates, maxpair)   #Returns the highest pair with its sum (which will have been the highest)
