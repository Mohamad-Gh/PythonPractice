def main():
    get = input("Expression: ")
    x, y, z = get.split(" ")
    print (float (calculate (x, y, z)))


def calculate(o, t, h):
    first = int(o)
    third = int(h)
    if t == "+":
        cal = first + third
    elif t == "-":
        cal = first - third
    elif t == "*":
        cal = first * third
    elif t == "/":
        cal = first / third
    return cal

main()
