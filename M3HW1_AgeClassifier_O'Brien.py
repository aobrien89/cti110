# CTI-110 
# M3HW1 - Age Classifier 
# Anthony O'Brien 
# 09/14/2017
#
def main():
    age = float(input("Age of person: "))
    if age <= 1:
        print("This person is an infant.")
    elif age <= 12 and age >= 2:
        print("This person is a child.")
    elif age <=19 and age >= 13:
        print("This person is a teenager.")
    elif age >= 20:
        print("This person is an adult.")
main()
