def main():
    text = input("Input: ")
    print(shorten(text))


def shorten(word):
    print("Output: ", end="")
    script = ""
    for letter in word:
        if letter.lower() =='a' or letter.lower() =="e" or letter.lower() == 'i' or letter.lower() == 'u' or letter.lower() == 'o':
            continue
        else:
            script = script + letter
    return script

if __name__ == "__main__":
    main()
