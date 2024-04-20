from inflect import engine
p = engine()
list=[]
while True:
    try:
        name = input("Name")
        list.append(name)
    except EOFError:
        print(f"Adieu, adieu, to {p.join(list)}")
        break

