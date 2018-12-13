# Lab 08 Jack Pierrepont and Brendon Luu
#03/28/2017
#The in-lab tutors were a big help with this as were the tutors at open lab.
#We Couldn't have done it without them!! :)




def encodeTXT():
    '''
    This is the main or umbrella function. It asks the user for a text file and
    key and encrypts the text file with the given key. The now encrypted text
    file is saved as encoded.txt
    ''' 
    key=input("Please enter the Vigenere key that you'd like to use? ")
    filename=input("Please enter the name of the file you wish to be encrypted: ")   
    plainTXT=open(filename)
    encodedFile=open("encoded.txt", "w")
    indx=0   
    for line in plainTXT:       
        encodedLine, indx=encryptLine(line, key, indx)
        encodedFile.write(encodedLine)

    print(filename,"has been encoded and written in a file called encoded.txt")
    plainTXT.close()
    encodedFile.close()




    
def encryptLine( line_str, key, key_idx ):
    '''
    str, str, int -> str
    This function takes an encoded line from a file as well as that file's key
    and uses the Vigenere encryption in reverse to "decode" the inputed line of text.
    '''
    cipher_str = ''
    for i in range(len(line_str)):
            if line_str[i]=='\n':
                key_idx=(i + key_idx) % len(key) 
                return (cipher_str + '\n'), key_idx
            else:
                charVal=ord(line_str[i]) - ord('A')
                keyVal=ord( key[(i + key_idx) % len(key)] ) - ord('A')
                encodedVal=(charVal + keyVal) % 26
                encodedChar=chr(encodedVal+ ord('A')) 
                cipher_str+=encodedChar


    
