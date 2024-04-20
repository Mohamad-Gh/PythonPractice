import sys
import requests

# Expects the user to specify as a command-line argument the number of Bitcoins if they dont we exit
if len(sys.argv)!= 2:
    sys.exit("Missing command-line argument")
    # If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.
try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    get = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    respond = get.json()
except requests.RequestException:
    sys.exit("Something went wrong with request function")
o, m = respond["bpi"]["USD"]["rate"].split(",")
num = n* float(o+m)
print(f"${num:,.4f}")

