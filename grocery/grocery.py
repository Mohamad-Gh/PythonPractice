def main():
    dict = get()
    printing(dict)

def get():
    grocery_list = {}
    while True:
        try:
            x = input().upper()
            # generate value of dict if it's in the dict already
            if x in grocery_list:
                grocery_list[x] += 1
            else:
                grocery_list[x] = 1
        except EOFError:
            break
        except KeyError:
            pass
    return grocery_list

def printing(g_list):
    #sorting dict based on its keys
    g_list =dict(sorted(g_list.items()))
    # iteriate to print like what requested
    for item in g_list:
        print(g_list[item], item)


main()
