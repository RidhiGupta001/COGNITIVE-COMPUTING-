import random

##random numbers from 1-10
r_integer = random.randint(1,10)
print("random integer = ", r_integer)

##random shuffle list
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print("Shuffled List:", numbers)

##randomly shuffle the list
colors = ["red", "blue", "green", "yellow", "purple"]
random_choice = random.choice(colors)
print("Random Choice from List:", random_choice)

##random dice 
dice = random.randint(1,6)
print("dice says = ",dice)