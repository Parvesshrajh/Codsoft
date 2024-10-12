import random

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"
symbols = "!@#$%^&*()."

strings = upper+lower+numbers+symbols
leng = int(input("Password Length:"))
password = "".join(random.sample(strings,leng))

print("Your password is : ",password)
