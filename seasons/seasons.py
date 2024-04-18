from datetime import date
import sys
import inflect

p = inflect.engine()
# implement a program that prompts the user for their date of birth in YYYY-MM-DD
# format and then prints how old they are in minutes,
def main():
    age = age_calculator(input("Date of Birth? "))
    print(age, "minutes")
def age_calculator(input):
    try:
        year, month, day = input.split("-")
        age = date(int(year), int(month), int(day))
        old = date.today() - age
        out = inflect.engine().number_to_words(round(old.total_seconds()/60), andword="")
        return out.capitalize()
    except ValueError:
        sys.exit("Invalid Date")

if __name__ == "__main__":
    main()
