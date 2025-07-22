age = int(input("enter your age:"))
if age < 13:
    print("you are a child")
elif 13 <= age <= 19:
    print("you are a teenager")
elif 20 <= age <= 64:
    print("you re an adult")
else:
    print("you are a senior")            