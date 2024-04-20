def main():
    frac = input("Fraction: ")
    first = convert(frac)
    print(gauge(first))

# prgogram for calling and checking the input
def convert(x):
    # requests input if wrong data is provided by user
    y, z = x.split("/")
            # calculate the fraction in case of getting zeroDivisionError and user input float numbers as well
    count = int(y)/int(z)
    if count > 1:
        raise ValueError
    return round(count*100)


# calculates and print the out put
def gauge(frac):
    if 0 <= frac <= 1:
        return "E"
    elif 99 <= frac <= 100:
        return "F"
    else:
        return f"{round(frac)}%"

if __name__ == "__main__":
    main()
