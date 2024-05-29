#program to calculate min number of guess

lower_bound=int(input("Enter the lower bound "))
upper_bound=int(input("Enter the upper bound "))

import random,math

x=random.randint(lower_bound,upper_bound)
print("\n\tYou've only ", 
       round(math.log(upper_bound - lower_bound + 1, 2)),
      " chances to guess the integer!\n")

count=0

while count<round(math.log(upper_bound - lower_bound + 1, 2)):
    count+=1
    guess=int(input("Enter the guess"))
    if x == guess:
        print("Congratulations you did it in ",
              count, " try")
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You Guessed too high!")

if count >= math.log(upper_bound - lower_bound + 1, 2):
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next time!")