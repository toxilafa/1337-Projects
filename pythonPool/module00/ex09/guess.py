from random import randint
import sys

print("This is an interactive guessing game!")
print("You have to enter a number between 1", end="")
print(" and 99 to find out the secret number.")
print("Type 'exit' to end the game.\nGood luck!\n")
counter = 0
goal = randint(1, 99)
while True:
    print("What's your guess between 1 and 99?")
    counter += 1
    attempt = input(">> ")
    if attempt.isdigit() is True:
        attempt = int(attempt)
        if attempt > goal:
            print("Too high!")
        if attempt < goal:
            print("Too low!")
        if attempt == goal and goal == 42:
            print("The answer to the ultimate question of life,", end="")
            print(" the universe and everything is 42.")
            if counter == 1:
                print("Congratulations! You got it on your first try!")
            else:
                print("You won in %d attempts!" % (counter))
            sys.exit()
        if attempt == goal:
            if counter == 1:
                print("Congratulations! You got it on your first try!")
            else:
                print("Congratulations, you've got it!")
                print("You won in %d attempts!" % (counter))
            sys.exit()
    elif attempt == "exit":
        print("Goodbye!")
        break
    else:
        print("That's not a number.")
