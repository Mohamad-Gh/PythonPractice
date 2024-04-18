
def main():

    change=get()
    print(cal(change))

def get():
    while True:
        try:
            money = float(input("Change: "))
            if money >= 0:
                return money
            else:
                continue
        except ValueError:
            continue

def cal(change):
    change*=100
    list = [25, 10, 5, 1]
    sum_numb = []
    for i in list:
        sum_numb.append(change // i)
        change = change % i
    return int(sum(sum_numb))


if __name__=="__main__":
    main()
