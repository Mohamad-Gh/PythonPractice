from validator_collection import validators,checkers,errors

def main():
    email = input("What's your email? ")
    print(response(email))

def response(s):
    try:
        if validators.email(s):
        # if checkers.is_email(s):
            return "Valid"
        else:
            return "Invalid"
    except ValueError:
        return "Invalid"
if __name__=="__main__":
    main()


