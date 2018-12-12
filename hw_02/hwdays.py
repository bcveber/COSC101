# ----------------------------------------------------------
# --------             HW 2: Days Later            ---------
# ----------------------------------------------------------

# ----------------------------------------------------------
# Please answer these questions after having completed this
# program
# ----------------------------------------------------------
# Name: Brian Veber
# Hours spent on program 3: 4.5
# Collaborators and sources: Tutor, Shamarcus Doty
#   (List any collaborators or sources here.)
# ----------------------------------------------------------


# Change this line to run_main = True if you want the input/output
# part of the program to run
#
# Otherwise, leaving it False allows you to easily test individual functions
run_main = False


# Complete the code for the six functions described in the instructions below
# Once you write code for a function, you can remove the line that says "pass"

def isLeapYear(year):
    ''' write your docstring here '''
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def daysInYear(year):    
    ''' write your docstring here '''
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return 366
            else:
                return 365
        else:
            return 366
    else:
        return 365
    
def daysInMonth(month, year):
    ''' write your docstring here '''
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    if month in (4,6,9,11):
        return 30
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return 29
            else:
                return 28
        else:
            return 29
    else:
        return 28
    
def dayNumber(year, month, day):
    ''' write your docstring here '''
    total = 0
    for num in range (month-1):
        total+=daysInMonth(num+1, year)
    total+=day-1
    return total
    
def daysUntilNewYear(year, month, day):
    ''' write your docstring here '''
    n = daysInYear(year) - dayNumber (year,month,day)
    return n
def daysLater(year1, month1, day1, year2, month2, day2):
    ''' write your docstring here '''
    total_days = 0
    if year1 == year2:
        for year in range (year1, year2):
            total_days = total_days + daysInYear(year)
        return total_days + daysUntilNewYear (year1, month1, day1) + dayNumber (year2, month2, day2) - daysInYear(year1)
    elif year1 != year2:
        for year in range (year1+1, year2):
            total_days = total_days + daysInYear(year)
        return total_days + daysUntilNewYear (year1, month1, day1) + dayNumber (year2, month2, day2)

print (daysLater(2016,5,17,2017,5,18))
        
# Main program
# do not modify the file below this

def main():
    print('Earlier date')
    year1 = int(input('Year: '))
    month1 = int(input('Month: '))
    day1 = int(input('Day: '))
    
    print()
    print('Later date')
    year2 = int(input('Year: '))
    month2 = int(input('Month: '))
    day2 = int(input('Day: '))
    
    print()
    answer = daysLater(year1, month1, day1, year2, month2, day2)
    print(answer, "days")

if __name__ == '__main__' and run_main:
    main()
