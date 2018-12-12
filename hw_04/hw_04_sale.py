# ----------------------------------------------------------
# --------             HW 4: Price Drop            ---------
# ----------------------------------------------------------

# ----------------------------------------------------------
# Please answer these questions after having completed this
# program
# ----------------------------------------------------------
# Name:
# Hours spent on program 1:
# Collaborators and sources:
#   (List any collaborators or sources here.)
# ----------------------------------------------------------


# Write your two functions for the price drop question here

def discount(price):
    '''
    str ---> int
    Takes a price and applies a 20% discount to that price, returning the
    discounted price. If discount is more than $100, the discount will be maxed
    out at $100 and only apply a $100 discount to the original price.
    '''
    
    if price == "":
        return ""
    percent_off = price * 0.20
    lower_price = price - percent_off
    if percent_off > 100:
        return round (price-100, 2)
    else:
        return round(lower_price, 2)

def faresale(T,C):
    list_flights = []
    
    for row in range (len(T)):
        entire_discount = [ ]
        for col in range (len(T[row])):
            if row in C: #discount
                discounted_price = discount(T[row][col])
                entire_discount = entire_discount + [discounted_price]
            elif col in C:
                discounted_price = discount(T[row][col])
                entire_discount = entire_discount + [discounted_price]
            else:
                entire_discount = entire_discount + [T[row][col]]
        list_flights = list_flights +[entire_discount]
    return list_flights
