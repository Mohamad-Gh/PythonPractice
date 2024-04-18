import sys
from tabulate import tabulate
import csv



def main():
    file_text = check_command_line_arg(sys.argv)
    print(tabulate(file_text[1:],file_text[0], tablefmt="grid"))



def check_command_line_arg(command_list):
   list = []
   reader ={}
   if len(command_list) < 2:
       sys.exit("Too few command-line arguements")
    # If the user does not specify exactly one command-line argument.
   elif len(command_list)>2:
        sys.exit("Too many command-line arguments")
        #  if the specified file’s name does not end in .csv
   elif command_list[1].endswith(".csv")==False:
        sys.exit("Not a CSV file")
        # if the specified file does not exist
   try:
        with open(command_list[1]) as table:
            reader = csv.reader(table)
            for line in reader:
                list.append(line)
            return list
   except FileNotFoundError:
        sys.exit("File doesn't exist")



if __name__ == "__main__":
    main()