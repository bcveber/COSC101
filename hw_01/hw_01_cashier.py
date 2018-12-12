# ----------------------------------------------------------
# --------              HW 1: Cashier              ---------
# ----------------------------------------------------------

# ----------------------------------------------------------
# Please answer these questions after having completed this
# program
# ----------------------------------------------------------
# Name: Brian Veber
# Hours spent on program 2: 1.5 hour
# Collaborators and sources: N/A
#   (List any collaborators or sources here.)
# ----------------------------------------------------------


# Write your python program for the cashier problem here

#Brian Veber, Check Out

#Collect name, amount spent, and amount paid
name = input("What is the customer's name: ")
spend = float(input("How much did " + name + " spend? "))
pay = float(input("$How much did " + name + " pay? "))

#Create the remainder, or change to be given
remainder = float(pay-spend)

#Divide and multiply accordingly, dividing by the same denomination and consecutively adding the previous denomination

dollars = int(remainder/1)
quarters = int((remainder-dollars)/.25)
dimes = int((remainder-dollars-(quarters*.25))/.10)
nickels = int((remainder-dollars-(quarters*.25)-(dimes*.10))/.05)
pennies = round(((remainder-dollars-(quarters*.25)-(dimes*.10)-(nickels*.05))/.01))

#Print the balance including the proper forms of money

print("$You owe", name, "$"+str(remainder), "("+str(dollars), "dollars,", quarters, "quarters,", dimes, "dimes,", nickels, "nickels, and", pennies, "pennies)")

#Tested all four examples including special cases such as 100 and 0, 1000 and 500.
