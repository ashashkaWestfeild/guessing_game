import random


#generate a randomnumber between 1 and 100
randnum = random.randint(1,101)

count = 0
guess = -99

while (guess != randnum):
    # Get the user's guess
    guess=(int)(input("Enter your guess between 1 and 100: "))
    if guess < randnum:
        print("Guess Higher")
    elif guess > randnum:
        print("Guess Lower")
    else:
        print("You guessed it!")
        break
    count = count + 1
# End of while loop

print("You took " + str(count) + " steps to guess the number")
