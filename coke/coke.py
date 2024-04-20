def main(amount_due = 50):
    cash = ask (amount_due)
    coins(cash, amount_due)
    machine (cash, amount_due)

def ask (m):
    print (f"Amount Due: {m}")
    money = int(input("Insert Coin: "))
    return money


def coins(n, b):
    while True:
        if  (n==25 or n==10 or n==5):
            break
        else:
            ask (b)


def machine(value, c):
    remain = c - value
    while remain > 0:
        value = ask (remain)
        coins(value, remain)
        remain = remain - value
    print(f"Change Owed: {-remain}")



main ()
