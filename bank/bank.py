def main ():
    hey = input ("Greeting:")
    print (bank(hey))

def bank(greeting):
    greeting = greeting.strip().lower()
    if "hello" in greeting:
        money = "$0"
    elif greeting[0] == 'h':
        money = "$20"
    else:
        money = "$100"
    return money

main ()
