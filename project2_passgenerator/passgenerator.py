import string
import random

def gen():
    s1=string.ascii_letters
    s2=string.digits
    s3=string.punctuation
    s = s1+s2+s3
    count=random.randint(8,12)
    password=""
    i=0
    while (count>i):
        i+=1
        password+=random.choice(s)
    return password

print(gen())