def main():
    text = input("Input: ")
    making_short(text)



def making_short(script):
    print("Output: ", end="")
    for letter in script:
        if letter.lower() =='a' or letter.lower() =="e" or letter.lower() == 'i' or letter.lower() == 'u' or letter.lower() == 'o':
            continue
        else:
            print(letter, end="")
    print("")
main()
