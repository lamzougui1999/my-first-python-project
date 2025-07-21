#simple program to calculate the sum of two numbers
#ask the user to enter two numbers
num1 = input("Enter first number: ")
num1_float = float(num1)
num1_int = int(num1_float)
num2 = input("Enter second number: ")
num2_float = float(num2)
num2_int = int(num2_float)
#calculate the sum of the two numbers
sum_result = num1_int + num2_int
#print the result
print("The sum of", num1_int, "and", num2_int, "is:", sum_result)