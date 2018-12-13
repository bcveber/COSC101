#Lab 10 Exceptions practice IOError:
#This program gets a file and displays contents to the screen
def main():
    #Get the file name
    filename = input ('Enter a filename: ')
    #Open the file
    infile = open(filename, 'r')
    #Read the file contents
    contents = infile.read()
    #Display the file contents
    print (contents)
    infile.close()
#Call the main function
main()
