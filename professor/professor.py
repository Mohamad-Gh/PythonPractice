import random

def main():
    freq = 10
    level = get_level()
    print(f"Score: {generate(level, freq)}")


def get_level():
    # Prompts the user for a level,If the user does not input 1, 2, or 3, the program should prompt again.
    while True:
        try:
            ask = int(input("Level: "))
            if 0< ask <4:
                return ask
        except ValueError:
            pass
# Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with level
# digits. No need to support operations other than addition (+).
def generate(number, count):
    score = 0
    round = 1
    for _ in range (count):
        # to random between 0 and 9
        if number == 1:
            a = random.randint(10**(number-1)-1, (10**number)-1)
            b = random.randint(10**(number-1)-1, (10**number)-1)
        else:
            # to between 10 to 99 or 100 to 999
            a = random.randint(10**(number-1), (10**number)-1)
            b = random.randint(10**(number-1), (10**number)-1)
        while True:
            #try:
                print(f"{a} + {b} = ", end= "")
                get = int(input(""))
                if get == a + b:
                    # to count the correct score of user
                    score +=1
                    break
                else:
                    round +=1
                    print("EEE")
            #except ValueError:
                #pass
            # TO ASK ONLY THREE TIMES AND SHOWS THE RESULTS ON THE FOURTH TIME
                if round == 4:
                    print(f"{a} + {b} = {a+b}")
                    break
    return score

if __name__ == "__main__":
    main()
