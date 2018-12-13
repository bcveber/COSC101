# Lab 10 Spring 2017

import random

def main_dict():
    # Initialize dictionary
    capitals = {'Alabama':'Montgomery', 'Alaska':'Juneau',
                'Arizona':'Phoenix', 'Arkansas':'Little Rock',
                'California':'Sacramento', 'Colorado':'Denver',
                'Connecticut':'Hartford', 'Delaware':'Dover',
                'Florida':'Tallahassee', 'Georgia':'Atlanta',
                'Hawaii':'Honolulu', 'Idaho':'Boise',
                'Illinois':'Springfield', 'Indiana':'Indianapolis',
                'Iowa':'Des Moines', 'Kansas':'Topeka',
                'Kentucky':'Frankfort', 'Louisiana':'Baton Rouge',
                'Maine':'Augusta', 'Maryland':'Annapolis',
                'Massachusetts':'Boston', 'Michigan':'Lansing',
                'Minnesota':'Saint Paul', 'Mississippi':'Jackson',
                'Missouri':'Jefferson City', 'Montana':'Helena',
                'Nebraska':'Lincoln', 'Nevada':'Carson City',
                'New Hampshire':'Concord', 'New Jersey':'Trenton',
                'New Mexico':'Santa Fe', 'New York':'Albany',
                'North Carolina':'Raleigh', 'North Dakota':'Bismarck',
                'Ohio':'Columbus', 'Oklahoma':'Oklahoma City',
                'Oregon':'Salem', 'Pennsylvania':'Harrisburg',
                'Rhode Island':'Providence', 'South Carolina':'Columbia',
                'South Dakota':'Pierre', 'Tennessee':'Nashville',
                'Texas':'Austin', 'Utah':'Salt Lake City',
                'Vermont':'Montpelier', 'Virginia':'Richmond',
                'Washington':'Olympia', 'West Virginia':'Charleston',
                'Wisconsin':'Madison', 'Wyoming':'Cheyenne'}
    return capitals

def state_list():
    random_state = ''
    random_list = []
    correct_count = 0
    incorrect_count = 0
    capital_input = ''

    maindict = main_dict()
    state_list = list(maindict)
    #print (random_state)

    while capital_input != '0':
        random_state = random.choice(state_list)
            
        capital_input = input ('What is the capital of' + ' ' + random_state + '? (or enter 0 to quit):')
        state_list.remove(random_state)
        
        if maindict[random_state] == capital_input:
            print ('That is correct.')
            correct_count += 1
        if maindict[random_state] != capital_input:
            print ('That is incorrect.')
            incorrect_count += 1

    print ('You had', correct_count, 'correct response and', incorrect_count, 'incorrect response.')
                
def main():
            
            
        

