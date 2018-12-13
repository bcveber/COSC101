#Appropriate variables
lot_number = 0

def lotnumber ():
    '''
    Prompts the user for the lot number. If the lot number does not equal 0, then
    it will do the show_tax.
    '''
    lotnuminput = int(input("Enter the lot number: "))
    while lotnuminput != 0:
        show_tax()
        lotnuminput = int(input("Enter the lot number: "))

       
def show_tax ():
    '''
    Prompts user for the value of the property.Shows tax of the using the equation
    property_value multiplied by *.0065.
    '''
    property_value = int(input("What is the property value? "))
    property_tax = property_value * 0.0065
    print('Your property tax is', property_tax)

#Add lotnumber and show_tax together:
def main():
    lotnumber()

#Print main
main()
    
