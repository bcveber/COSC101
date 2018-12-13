#Study Guide

#Problem 1

def streaks(num_list):
    count = 0
    streak_count = 0

    for num in num_list:
        if num == 0:
            count = 0
        if num != 0:
            count += 1
        if count == 1:
            streak_count += 1
            
    return streak_count

##
##print(streaks([0, 3, 2, 1, 3, 0]))
##print(streaks([0, 3, 2, 1, 3, 0, 2]))


#Problem 2

def streaks_2(num_list):
    count = 0
    streak_count = 0

    for num in num_list:
        if num == 0:
            count = 0
        if num != 0:
            count += 1
        if count == 3:
            streak_count += 1
            
    return streak_count

##print(streaks_2([0, 3, 2, 1, 3, 0, 2]))
##print(streaks_2([0, 3, 2, 2, 0, 3, 2]))
##print(streaks_2([3, 2, 1, 0, 3, 2, 1, 3, 0, 1, 1, 2]))


#Problem 3

def month_dictionary(month_dict):

    final_list = []
    bad_list = []
    for month in month_dict:
        first_dict_value = month_dict[month]
        #print(first_dict_value)
        for item in first_dict_value:
            second_dict_value = first_dict_value[item]
            if len(second_dict_value) >= 2:
                bad_list += [month]
            if len(second_dict_value) < 2:
                final_list += [month]
                
    very_final_list = []
    for x in final_list:
        if x not in very_final_list and x not in bad_list:
            very_final_list += [x]
            
    return very_final_list
                

    
example = {"February" : {13 : ["Catherine"]},
     "May" : {3 : ["Katie"], 8 : ["Peter", "Ed"]},
     "December" : {12 : ["Sharon"], 22 : ["Owen"]}
        }

print(month_dictionary(example))
