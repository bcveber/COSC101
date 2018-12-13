#Brian Veber, Lab02

#Lab02.3

hippo_weight = float(input('How much does the pregnant hippo weigh? '))
calf_weight = int(input('How much does the calf weigh? '))
food_pounds = float(input ('How much food in pounds does the hippo eat? '))
print("If a pregnant hippo, weighing", int(hippo_weight), "pounds, gives birth to a", str(calf_weight)+"-pound calf, but then eats", int(food_pounds), "pounds of food, how much does she weigh?")
cumaltive_weight = hippo_weight - calf_weight + food_pounds
input("Press the enter key to find out")
print("The poor hippo weighs", int(cumaltive_weight), "pounds")

#Pirates

pirate_count = float(input("How many pirates are there? "))
gold_coins = float(input("How many coins did the pirates find? "))
print ("If a group of", int(pirate_count), "pirates finds a chest full of", int(gold_coins), "gold coins, and they divided the booty evenely, how many coins will be left over?")
left_overs = gold_coins%pirate_count
input("Press the enter key to find out")
print("The pirates will fight over the remaining", int(left_overs), "pieces of gold coins")
