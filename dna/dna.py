import csv
import sys


def main():

    # TODO: Check for command-line usage
    check_input(sys.argv)

    # TODO: Read database file into a variable
    csv_list =[]
    with open(sys.argv[1]) as csvfile:
        csv_reader = csv.DictReader(csvfile)
        str_list = csv_reader.fieldnames
        for row in csv_reader:
            csv_list.append(row)

    # TODO: Read DNA sequence file into a variable
    with open(sys.argv[2]) as dna_file:
        dna_reader = dna_file.read()

    # TODO: Find longest match of each STR in DNA sequence
    test_dna = {}
    for str in str_list[1:]:
        test_dna[str]=longest_match(dna_reader,str)
    print(test_dna)

    # TODO: Check database for matching profiles
    print(check_id(test_dna,str_list,csv_list))

def check_input(argv):
        try:
            if len(argv)!=3:
                sys.exit("wrong input number")
            if argv[1].strip().endswith(".csv") and argv[2].strip().endswith(".txt"):
                return True
            else:
                return False
        except FileNotFoundError:
            sys.exit("File not found")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


def check_id(numbers, list, file):
    print(len(list))
    response ="No match"
    for row in file:
        k = 0
        for key in list[1:]:
            if int(row[key])== numbers[key]:
                k+=1
                print(row[list[0]])
                print(k)
                if k == len(list)-1:
                    response = row[list[0]]
            else:
                break
    return response


if __name__=="__main__":
    main()
