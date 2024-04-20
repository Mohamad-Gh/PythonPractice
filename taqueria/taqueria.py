def main ():
    call()

def call():
    dict = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    sum = 0
    while True:
        try:
           x = input("Item: ").title()
           sum += dict[x]
           # to print with 2 decimal point
           print(f"Total: ${sum:.2f}")
           # to quit the program with control-d command
        except EOFError:
           print("\n", end="")
           break
        except KeyError:
            pass


main()
