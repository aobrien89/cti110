# Converts kilometers to miles
# 10/24/2017
# CTI-110 M6T1_KilometerConversion 
# Anthony O'Brien
#
INCHES_PER_FOOT = 12

def main():
    feet = int(input("Enter a number of feet: "))
    print(feet, "ft equals", feet_to_inches(feet), "inches")

def feet_to_inches(feet):
    return feet * INCHES_PER_FOOT

main()
