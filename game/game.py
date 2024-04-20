import random
import sys

def main():
    n = asking()
    # Randomly generates an integer between 1 and n, inclusive, using the random module.
    num = random.randint(1, n)
    check(num)


# Prompts the user for a level n, If the user does not input a positive integer, the program should prompt again.
def asking():
    while True:
        try:
            ask = int(input("Level: "))
            if ask > 0:
                return ask
        except ValueError:
            pass

def check(randnum):
        while True:
            try:
            # Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
                guess = int(input("Guess: "))
            except ValueError:
                continue
            if guess < 1:
                continue
            elif guess > randnum:
                print("Too Large!")
            elif guess < randnum:
               print("Too small!")
            else:
                print("Just right!")
                sys.exit()


main()
