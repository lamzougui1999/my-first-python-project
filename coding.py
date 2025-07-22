name = input("enter your name:")
age = int(input("enter your age:"))
future_age = age + 5
if age % 2 == 0:
    parity = "even"
else:
    parity = "odd"
    
if age < 13:
    molity = "child"
elif 13 <= age <= 19:
    molity = "teenager"
elif 20 <= age <= 64:
    molity = "adult"
else:
    molity = "senior"

if molity[0] in "aeiou":
    article = "an " + molity
else:
    article = "a " + molity

print("hello " + name + "! in 5 years you will be " , future_age , " your age is " + parity + ". you are " + article +".")

# This code determines the user's age category and provides a greeting with future age and parity information.
# 9:14 AM 07/22/2025 California, USA