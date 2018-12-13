total_slices = 0

def num_pizzas (adults, boys, girls):
    '''
    (int, int, int) --> int
    Adults, boys, and girls order pizza slices with a ratio for each type of person and 8 slices of pizza make one whole pizza.
    '''
    adults_pizza = adults * 2
    boys_pizza = boys * 3
    girls_pizza = girls * 1
    total_slices = adults_pizza + boys_pizza + girls_pizza
    if total_slices % 8 == 0:
        return (total_slices / 8)
    else:
        return (total_slices // 8 + 1)
        
print(total_slices = num_pizzas(1,1,1))

