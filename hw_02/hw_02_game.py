# ----------------------------------------------------------
# --------           HW 2: Game Winner             ---------
# ----------------------------------------------------------

# ----------------------------------------------------------
# Please answer these questions after having completed this
# program
# ----------------------------------------------------------
# Name: Brian Veber
# Hours spent on program 1:
# Collaborators and sources:
#   (List any collaborators or sources here.)
# ----------------------------------------------------------


# Write your python program for the Game Winner problem here
points = 0
players = int(input("Number of players: "))
players_second = players
rounds = int(input("Number of rounds: "))
player_scores = [0] * players
highest_score = 0
print()
for i in range (rounds):
    print ("Round", (i+1))
    for k in range (players):
        points_each = int(input ("Player " + str((k+1)) + ': '))
        player_scores[k]+= points_each                        
    print() 

print ('Final Scores')
for z in range (players):
    print ("Player", str((z+1)) + ':', player_scores[z])
    if player_scores[z] > highest_score:
        highest_score = player_scores[z]
        highest_player = z
print()
print ("The winner is Player", str(highest_player+1) + '!')
        
             
