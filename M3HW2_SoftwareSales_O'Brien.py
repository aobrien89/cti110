# CTI-110 
# M3HW2 - Software Sales
# Anthony O'Brien 
# 09/19/2017
#
def main():
    purchase = float(input("Packages purchased: "))
    if purchase <= 9:
        print("No discount :(")
    elif purchase <= 19:
        print("10% discount!")
    elif purchase <= 49:
        print("20% discount!")
    elif purchase <= 99:
        print("30% discount!")
    elif purchase >= 100:
        print("40% discount!")

main()
