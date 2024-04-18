import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    try:
        part= re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$", ip)
        if (0<=int(part.group(1))<=255 and 0<=int(part.group(2))<=255
            and 0<=int(part.group(3))<=255 and 0<=int(part.group(4))<=255
            ):
            return True
    except AttributeError:
        return False
    return False


...


if __name__ == "__main__":
    main()