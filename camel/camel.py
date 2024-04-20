def main ():
    ask = input ("camelCase: ")
    snake(ask)


def snake(word):
    for i in word:
        if i.islower():
            print(i, end="")
        else:
            print(f"_{i.lower()}", end="")

main()
