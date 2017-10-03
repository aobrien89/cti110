# CTI-110 
# M3LAB
# Anthony O'Brien
# 09/14/2017
#
def main():
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60
    F_score = 59
    
# TO DO: define the rest of the scores
    score = float(input("Enter grade: "))

    if score >= A_score:
        print('Your grade is: A')
    elif score >= B_score:
        print('Your grade is: B')
    elif score >= C_score:
        print('Your grade is: C')
    elif score >= D_score:
        print('Your grade is: D')
    elif score <= F_score:
        print('Your grade is: F')
        
# program start

main()
