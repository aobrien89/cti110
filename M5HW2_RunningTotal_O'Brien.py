# CTI-110 
# M5HW2 - Running Total
# Anthony O'Brien
# 10/12/2017

total = 0
currentNumber = 0

while currentNumber > -1:
    total = total + currentNumber
    currentNumber = float(input("Enter a number "))

print(total)
