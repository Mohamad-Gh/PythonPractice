def main():
    time = input ("what time is it? ")
    if 7<= convert (time) <=8 :
        print ("breakfast time")
    elif 12 <= convert (time) <=13 :
        print ("lunch time")
    elif 18 <= convert (time) <=19 :
        print ("dinner time")



def convert(time):
    x, y = time.split(":")
    cal =int (x) + int (y)/60
    return cal


if __name__ == "__main__":
    main()
