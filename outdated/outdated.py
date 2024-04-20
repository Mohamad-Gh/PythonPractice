def main():
    call()



def call():
    while True:
        try:
            ask = input("Date: ")
            if  check_format(ask) == False:
                continue
            else:
                year, mon, day = check_format(ask)
                print(f"{year:02}-{mon:02}-{day:02}")
                break
        except ValueError:
            pass


def check_format(date):
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]
    if "/" in date:
        month, day, year = date.split("/")
        month = int(month)
        day = int(day)
        year = int(year)
        if month>12 or month<1:
            return False
        elif day >31 or day <1:
            return False
        return year, month, day
    elif ", " in date and " " in date:
        mon_day , year = date.split(", ")
        mont , day = mon_day.split(" ")
        year = int (year)
        day = int(day)
        mont = months.index(mont.title())+1
        if day >31 or day <1:
            return False
        return year, mont, day
    else:
        return False


main()
