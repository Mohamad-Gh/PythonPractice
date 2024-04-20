import sys
from pyfiglet import Figlet

if len(sys.argv)== 1:
    ask = input("Input: ")
    print(Figlet.renderText(ask))
elif len(sys.argv)== 3:
    if sys.argv[1] == "-f" or sys.argv[1]=="-font":
        f= Figlet()
        if sys.argv[2] not in f.getFonts():
            sys.exit("wrong font name")
        ask = input("Input: ")
        f.setFont(font=sys.argv[2])
        print(f.renderText(ask))
    else:
        sys.exit("worng code use -f or -font as second argument")
else:
    sys.exit("wrong command line number")

