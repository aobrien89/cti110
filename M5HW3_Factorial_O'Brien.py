# CTI-110 
# M5HW1 - Distance Traveled
# Anthony O'Brien
# 10/12/2017

userInteger = int(input("Please enter a nonnegative integer: "))
factorial = 1
for currentNumber in range(1, userInteger + 1):
                           factorial = factorial * currentNumber
print("The factorial of", userInteger, "is", factorial)                           
