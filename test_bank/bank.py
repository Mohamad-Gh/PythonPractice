def main ():
    hey = input ("Greeting:")
    print (value(hey))

def value(greeting):
    money = 0
    greeting = greeting.strip().lower()
    if "hello" in greeting:
        money = 0
    elif greeting[0] == 'h':
        money = 20
    else:
        money = 100
    return money

if __name__ == "__main__":
    main ()
