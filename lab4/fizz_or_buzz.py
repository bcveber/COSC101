#Brian Veber, Lab04, Fizz_or_Buzz.py

def fizz_or_buzz (number):
    '''
    (int) --> str
    Figure out if the number is divisible by 3 or 5 and print Fizz or Buzz. If
    divisible by both, then print FizzBuzz.
    '''
    if number %3 == 0 and number %5 == 0:
        return 'FizzBuzz'
    elif number % 3 == 0:
        return 'Fizz'
    elif number % 5 == 0:
        return 'Buzz'

def main ():
    for num in range (100):
        print(fizz_or_buzz(num+1))

print(main())

