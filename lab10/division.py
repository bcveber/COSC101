#Lab 10 Exceptions practice ZeroDivisionError
#This program divides a number by another number
def main():
    '''This program gets two numbers fro the user and then
divides the first number by the second number'''
    
    #Get two numbers
    num1 = int(input('Enter the first number:' ))
    num2 = int(input("Enter the second number: "))

    #Divide num1 by num2 and display the result.
    result = num1 / num2
    print(num1, 'divided by ' , num2, 'is' , result)
#Call the main function
main()
               
               
