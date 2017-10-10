# CTI-110 
# M5HW1 - Distance Traveled
# Anthony O'Brien
# 10/10/2017

speed = int(input("Speed? "))
hours = int(input("Hours? "))
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
traveled = 0
for num in list:
    traveled = speed * hours

print("distance traveled ", traveled)
