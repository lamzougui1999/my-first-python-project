name = input("enter your name:")
age = int(input("enter your age:"))
country = input("enter your country:")
work = input("enter your work:")


#count his age after 5 years 
future_age = age + 5

#choose if the age is odd or even
if age % 2 == 0:
    age_type = "even"
else:
    age_type = "odd"
     
# determine his age group
if age < 13:
    age_group = "child" 
elif 13 <= age <= 19:
    age_group = "teenager"
elif 20 <= age <= 64:
    age_group = "adult"
else:
    age_group = "senior"

# an a for age group
if age_group[0] in "aeiou":
    age_group_article = "an " + age_group
else:
    age_group_article = "a " + age_group

    # a an for country and work
if  work[0] in "aeiou":
    work_article = "an " + work
else:
    work_article = "a " + work

# print the the card 
print("hello " + name + " from " + country + "\nYou are " + age_group_article + " and your age is " + age_type + ".\nIn 5 years you will be " , future_age, ".\nYou are " + work_article + ".")



# This code  give  user's card information
# 9:14 AM 07/22/2025 California, USA