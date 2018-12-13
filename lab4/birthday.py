#Birthday Wishes
#Demonstrates keyword arguments and default parameter values

#positional parameters
def birthday1(name, age):
    print ("Happy birthday", name, "!", "I hear you're", age, "today./n")

#parameters with default values
def birthday2(name = "Katherine", age = 1):
    print ("Happy birthday", name, "!", "I hear you're", age, "today./n")

birthday1("Jackson", 13)
birthday1(1, "Buddy")
birthday1(name = "Karen", age = 12)
birthday1(age = 5, name = "Lila")

birthday2()
birthday2(name = "Amelia")
birthday2(age = 2)
birthday2(name = "Natalie", age = 10)
birthday2("Natalie", 12)

input("/n/nPress the enter key to exit.")
