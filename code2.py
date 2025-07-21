#my code Of today 07/21/2025 5:33AM CALIFORNIA
#this is a simple welcome program in python 
name = input("what is you re name? ") # i asked the customer to type his name
age = input("how old are you? ") #ask about age
country = input("where are you from? ") # ask about the country
#output the welcome message
print("hello, " + name + "!") #great the user
print("you are " + age + " years old.")
print("you are from " + country + ". welcome")
#new Qs
hobby = input("what is your favorite hobby? ")
likes_coding = input("do you like coding? (yes/no) ")
print("wow! " + hobby + " sound fun!")
if "yes" in likes_coding:
    print("thats great! coding is a powerfull skill! 💻")
elif "no" in likes_coding:
    print("No Worries! you might like it someday 😊")   
else:
    print("Hmmm... I didn't understand that. but coding is worth a try! 😁")     