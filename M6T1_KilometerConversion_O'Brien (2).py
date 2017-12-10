# Converts kilometers to miles
# 10/24/2017
# CTI-110 M6T1_KilometerConversion 
# Anthony O'Brien
#
CONVERSION_FACTOR = 0.6214

def main():
    kilometers = float(input("Enter a distance in kilometers: "))
    show_miles(kilometers)

def show_miles(km):
    miles = km * CONVERSION_FACTOR
    print(km, "kilometers equals", miles, "miles")

main()
