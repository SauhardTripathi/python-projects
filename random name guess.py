import random 
random_lst=['sauhard','tripathi','mani','tiwari']

word=random.choice(random_lst)
turns=10
print(word)
guesses=''
while turns>0:
    
    guess=input("enter the char ")

    for char in word:
        if char in guess:
            print(guess)
            guesses+=guess
        else:
            print(guess," not in ",word)
    turns-=1
    print(turns)
    print(guesses)
    if guesses==word:
        print("you win")
        break
    elif turns==0:
        print("you loose")
    else:
        print("you have to enter the number again")

