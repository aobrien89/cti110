# CTI-110 
# M3T1 - Areas of Rectangles 
# Anthony O'Brien
# 09/14/2017
#
print("Calculate the area of two rectangles")
length1 = float(input("Length of first rectangle: "))
width1 = float(input("Width of first retangle: "))
length2 = float(input("Length of second rectangle: "))
width2 = float(input("Width of second rectangle: "))
print("Area of first retangle:", length1 * width1)
print("Area of second rectangle:", length2 * width2)
area1 = length1 * width1
area2 = length2 * length2
if area1 > area2:
        print("The first rectangle has a greater area.", area1)
elif area1 < area2:
        print("The second rectangle has the greater area of", area2)
