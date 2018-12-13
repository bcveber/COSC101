#Brian Veber, Lab04, caught_speeding.py

def caught_speeding (speed, birthday):
    '''
    (int, int) --> int
    Driver is speeding and certain speeds equate to certain tickets. If it is
    the driver's birthday then he gets 5 extra miles to go over on the ticket
    basis.
    ticket
    >>>0,1,2
    '''
    ticket = 0
    if birthday == True:
        speed -= 5
    if speed <= 60:
        ticket = 0
    elif speed >= 61 and speed <= 80:
        ticket = 1
    elif speed >= 81:
        ticket = 2
    return ticket

print(caught_speeding(80, False))

