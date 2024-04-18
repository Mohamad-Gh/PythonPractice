import re

def main():
    text = get()
    point = point_cal(text)
    print(grade(point))

def get():
    text = input("Text: ")
    return text.strip()

def point_cal(text):
    letter = 0
    for i in text:
        if i.isalpha():
            letter += 1
        else:
            continue
    words = len(text.split(" "))
    sentences = len(text.split("."))+len(text.split("!"))+len(text.split("?"))-3
    L = letter * 100 // words
    S = sentences * 100 // words
    index = 0.0588 * L - 0.296 * S - 15.8
    return round(index)

def grade(index):
    if index >= 16:
        return "Grade 16+"
    elif index < 1:
        return "Before Grade 1"
    else:
        return f"Grade {index}"


if __name__=="__main__":
    main()