# Lab 10 one except clause

def main():
    # Declare variables
    total = 0.0
    number = 0.0
    counter = 0
    
    # Open numbers.txt file for reading
    infile = open('sales_data.txt', 'r')

    for line in infile:
        counter = counter + 1
        number = float(line)
        total += number
        
    # Close file
    infile.close()

    # Calculate average
    average = total / counter
    
    # Display the average of the numbers in the file
    print('Average: ', average)

# Call the main function.
main()

