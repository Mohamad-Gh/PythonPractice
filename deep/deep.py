def main ():
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    if check (answer):
        print("yes")
    else:
        print("No")


def check(respond):
    respond = respond.strip().lower()
    if respond == "42" or respond == "forty-two" or respond == "forty two" :
        return True
    else:
        return False

main()
