import sys
import csv


def main():
    in_file, out_file = command_line_arg_check()
    scourgify(in_file,out_file)

# check command_line arguments
def command_line_arg_check():
    # if the input is more than 3 words
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    # if the input is less than 3 words
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    # input name is not CSV
    if ".csv" not in sys.argv[1]:
        sys.exit(f"Could not read {sys.argv[1]}")
        # return the command-line arguments for the next code
    return sys.argv[1], sys.argv[2]


def scourgify(first, second):
    # we try to see if the file exist first
    try:
        with open(first, "r") as in_csv_file:
            reader = csv.DictReader(in_csv_file)
            # open the out_put file before closing the first one
            with open (second, "w") as out_csv_file:
                # defining the header and writing the header
                # Since the file is open to be write into we can use many write command in this section
                writer = csv.DictWriter(out_csv_file, fieldnames=["first", "last", "house"])
                writer.writeheader()
                for line in reader:
                    writer.writerow(split(line))
    # the error for couldn't find the file
    except FileNotFoundError:
        sys.exit(f"Could not read {first}")

# a program to get a dictionary and output dictionary based on the first, last, house output
def split(each):
    out_list={}
    last, first = each["name"].split(", ")
    out_list["first"]= first
    out_list["last"] = last
    out_list["house"]= each["house"]
    return out_list


if __name__=="__main__":
    main()
