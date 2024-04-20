import sys
import csv

def main():
    read_lines= input_check(sys.argv)
    print(lines_counter(read_lines))


# implement a program that expects exactly one command-line argument, the name (or path) of a Python file
def input_check(list):
    # If the user does not specify exactly one command-line argument.
    if len(list) < 2:
        sys.exit("Too few command-line arguements")
    # If the user does not specify exactly one command-line argument.
    elif len(list)>2:
        sys.exit("Too many command-line arguments")
    #  if the specified file’s name does not end in .py
    elif list[1].endswith(".py")==False:
        sys.exit("Not a Python file")
    # if the specified file does not exist
    try:
        with open(list[1], "r") as file:
            read = file.readlines()
            return read
    except FileNotFoundError:
        sys.exit("File doesn't exist")



# outputs the number of lines of code in that file, excluding comments and blank lines
def lines_counter(text):
    count_lines = 0
    for lines in text:
        if lines.lstrip().startswith("# "):
            continue
        elif lines.startswith("\n"):
            continue
        elif lines.lstrip().startswith(","):
            continue
        elif lines.isspace()==True:
            continue
        else:
            count_lines +=1
    return count_lines


if __name__=="__main__":
    main()
