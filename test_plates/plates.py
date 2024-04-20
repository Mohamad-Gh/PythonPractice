def main():
    plate = input("Plate: ")
    if is_valid(plate)==True:
        print("Valid")
    else:
        print("Invalid")


def is_valid(text):
    validity = True
    # vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.
    if len(text)> 6 or len(text) < 2:
        return False
    # No periods, spaces, or punctuation marks are allowed.
    # All vanity plates must start with at least two letters.
    if text.isalnum()==False or text[0:2].isnumeric():
        return False

    # No period ....
    # for c in text:
        # if c in [",", " ", ".", "!"]:
            #return False
        #else:
            #continue
    # Numbers cannot be used in the middle of a plate; they must come at the end.
    for i in range(len(text)-1):
        if text[i].isnumeric() and text[i+1].isalpha():
            return False
    # The first number used cannot be a ‘0’.”
    for j in range(2, len(text)-1):
        if text[i].isnumeric() and text[i+1].isnumeric() and text[i]=="0":
            return False
    # k = 0
    # while k < len(text):
        # if text[k].isnumeric():
            # if text[k]=="0":
                # return False
            # else:
                #break
        # k += 1
    return validity

if __name__=="__main__":
    main ()
