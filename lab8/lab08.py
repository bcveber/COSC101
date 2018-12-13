# Brodie Cohen, Brian Veber Lab 8

# Part 1

def open_file():
    '''
    Asks for the Vigenere key to be used. Asks for the file that is to be opened,
    and then goes on to open that file.
    '''
    key = input('What is the Vigenere key you want to use? ')
    txt_file = input('What is the name of the file to be encrypted? ')
    txt_file = open(txt_file, 'r')
    encrypt(txt_file, key)
    

def encrypt(txt_file, key):
    '''
    While there are still lines left in the file to be encoded, the while loop
    will run. Creates a new ling length based off the length of the line and the
    keys. Within the while loop, it takes the character of each letter in the file
    to be encrypted and of 'THEKEY' and adds them together to create a new
    str_encrypt value.
    '''
    line = ' '
    encoded_file = open('encoded.txt', 'w')
    while line !='':
        line = txt_file.readline()
        str_encrypt = ''
        length_line = (len(line)//len(key))
        long_key = (length_line*key) + (len(line)%len(key)*key) 
        for i in range(len(line)-1):
            ch_txt = line[i]
            ch_key = long_key[i]
            num_encrypt = add(ch_txt, ch_key)
            ch_encrypt = chr(num_encrypt + 65)
            str_encrypt += ch_encrypt
        
        encoded_file.write(str_encrypt)
    encoded_file.close()

def add(s1, s2):
    '''
    Subtracts 65 from the values of each letter of the encoded text and the individual
    letters in 'THEKEY.' Proceeds to encode the text by taking modulo 26. Returns the
    encrypted text.
    '''
    num_txt = ord(s1)-65
    num_key = ord(s2) -65
    ord_tot = num_txt + num_key
    num_encrypt = ord_tot % 26
    return num_encrypt

 #Part 2

def open_decrypt():
    '''
    Asks for the Vigenere key to be used. Asks for the file that is to be opened and
    decrypts the file.
    '''
    key = input('What is the Vigenere key you want to use? ')
    txt_file = input('What is the name of the file to be decrypted? ')
    txt_file = open(txt_file, 'r')
    decrypt(txt_file, key)

def decrypt(txt_file, key):
    '''
    Similar to def encrypt(), this program does the exact opposite. It takes a
    decrypted file and vigenere key such as 'THEKEY' and uses the key to reset the
    the text/file to what it was originally.
    '''
    line = ' '
    decoded_file = open('decoded.txt', 'w')
    while line != '':
        line = txt_file.readline()
        str_decrypt = ''
        length_line = (len(line)//len(key))+(len(line)%len(key))
        long_key = length_line*key
        for i in range(len(line)):
            ch_encrypt = line[i]
            ch_key = long_key[i]
            num_key = ord(ch_key) - 65
            num_encrypt = ord(ch_encrypt) - 65
            if num_encrypt > num_key:
                txt = subtract(num_key, num_encrypt)
            if num_encrypt < num_key:
                txt = mult(num_key, num_encrypt)
            if num_encrypt == num_key:
                txt = 'A'
            str_decrypt += txt
        decoded_file.write(str_decrypt)
    decoded_file.close()
            
                

def subtract(num_key, num_encrypt):
    '''
    Subtracts the num_encrypt value from the num_key value. Then turns this value into a
    ordinal value by adding 65, and returns this final  value.
    '''
    num_txt = num_encrypt - num_key
    ordinal_txt = num_txt + 65
    real_txt = chr(ordinal_txt)
    return real_txt

def mult(num_key, num_encrypt):
    '''
    Adds the num_encrypt value and 26 and subtracts that value to the num_key value. Then
    adds 654 to this value, and returns the new final value.
    '''
    num_txt = (26 + num_encrypt) - num_key
    ordinal_txt = num_txt + 65
    real_txt = chr(ordinal_txt)
    return real_txt
    
