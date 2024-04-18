import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
        if time:= re.search(r"(\d\d?):?(\d\d)? (AM|PM) to (\d\d?):?(\d\d)? (AM|PM)", s, re.IGNORECASE):
            time1 = time.group(1)
            time2 = time.group(2)
            time4 = time.group(4)
            time5 = time.group(5)
            if time.group(2) == None:
                time2 = "00"
            if time.group(5) == None:
                time5 = "00"
            if int(time1) >12 or int(time2)>59 or int(time4)>12 or int(time5)>59:
                raise ValueError
            if int(time1)<0 or int(time2)<0 or int(time4)<0 or int(time5)<0:
                raise ValueError
            if time.group(3) == "PM":
                if time1=="12":
                    time1="12"
                else:
                    time1 = str(int(time1)+12)
            if time.group(6) == "PM":
                if time4=="12":
                    time4="12"
                else:
                    time4 = str(int(time4)+12)
            if time.group(6)=="AM" and time4=="12":
                time4="00"
            if time.group(3) == "AM" and time1=="12":
                time1="00"
        else:
            raise ValueError
        return f"{int(time1):02}:{time2} to {int(time4):02}:{time5}"

...


if __name__ == "__main__":
    main()
