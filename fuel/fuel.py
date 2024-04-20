def main():
    first = calc()
    gauge (first)

# prgogram for calling and checking the input
def calc():
    # requests input if wrong data is provided by user
    while True:
        try:
            x = input("Fraction: ")
            y, z = x.split("/")
            # calculate the fraction in case of getting zeroDivisionError and user input float numbers as well
            count = int(y)/int(z)
            if count > 1:
                continue
            return count
        except ValueError:
            pass
        except ZeroDivisionError:
            pass


# calculates and print the out put
def gauge(frac):
    if 0 <= frac <= 0.1:
        print("E")
    elif 0.9 <= frac <= 1:
        print("F")
    else:
        print(f"{round(frac*100)}%")

if __name__ == "__main__":
    main()
