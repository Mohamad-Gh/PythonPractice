import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    link = re.search(r'^<iframe (\w+="[0-9]+" )*src="https?://(www\.)?youtube\.com/embed/(\w+)".*></iframe>$', s)
    if link:
        return f"https://youtu.be/{link.group(3)}"
    else:
        return "None"

...


if __name__ == "__main__":
    main()