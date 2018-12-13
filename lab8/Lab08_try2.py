# Brodie Cohen, Brian Veber Lab 8

# Part 1

def main_encrypt():
    '''
    Asks for the Vigenere key to be used. Asks for the file to encrypt.
    Saves encrypted file as encoded.txt.
    '''
    key = input('What is the Vigenere key you want to use? ')
    txt_file = input('What is the name of the file to be encrypted? ')
    txt_file = open(txt_file, 'r')
    encrypt(txt_file, key)
    

def encrypt(txt_file, key):
    '''(file, str) -> file
    Encrypts the given txt_file given the key. Returns the new encrypted file
    as encoded.txt.
    '''
    pos_key = 0
    encoded_file = open('encoded.txt', 'w')
    for line in txt_file:
        str_encrypt = ''
        key_encrypt = ''
        for i in range(len(line)-1):
            if pos_key == 6:
                pos_key = 0
            pos_key = (pos_key) % len(key)
            ch_txt = line[i]
            ch_key = key[pos_key]
            
            num_encrypt = add(ch_txt, ch_key)
            ch_encrypt = chr(num_encrypt + 65)
            str_encrypt += ch_encrypt
            key_encrypt += ch_key
            pos_key += 1
        
        print(key_encrypt)
        print(line)
            
        
        encoded_file.write(str_encrypt)
    return encoded_file
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

def main_decrypt():
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
    pos_key = 0
    decoded_file = open('decoded.txt', 'w')
    for line in txt_file:
        str_decrypt = ''
        for i in range(len(line)-1):
            if pos_key == 6:
                pos_key = 0
            pos_key = (pos_key) % len(key)
            ch_encrypt = line[i]
            ch_key = key[pos_key]
            num_key = ord(ch_key) - 65
            num_encrypt = ord(ch_encrypt) - 65
            if num_encrypt > num_key:
                txt = subtract(num_key, num_encrypt)
            if num_encrypt < num_key:
                txt = mult(num_key, num_encrypt)
            if num_encrypt == num_key:
                txt = 'A'
            str_decrypt += txt
            pos_key+=1
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
    
