# Takes input of test scores and displays letter grades.
# 11/12/2017
# CTI-110 M6HW1 - Test Average and Grade
# Anthony O'Brien
#

def main():
    score1, score2, score3, score4, score5 = ask_Scores()
    print()
    print_results(score1, score2, score3, score4, score5)
    

def ask_Scores():
    score1 = float(input("Enter first score: "))
    score2 = float(input("Enter second score: "))
    score3 = float(input("Enter third score: "))
    score4 = float(input("Enter fourth score: "))
    score5 = float(input("Enter fifth score: "))
    return score1, score2, score3, score4, score5

def print_results(score1, score2, score3, score4, score5):
    print("Score\tLetter Grade")
    print(str(score1) + "\t\t" + determine_grade(score1), \
          str(score2) + "\t\t" + determine_grade(score2), \
          str(score3) + "\t\t" + determine_grade(score3), \
          str(score4) + "\t\t" + determine_grade(score4), \
          str(score5) + "\t\t" + determine_grade(score5), sep = "\n")

def calc_average(score1, score2, score3, score4, score5):
    average = score1 + score2 + score3 + score4 + score5 / 5
    return average

def determine_grade(userscore):
    if userscore < 60:
        return "F"
    elif userscore < 70:
        return "D"
    elif userscore < 80:
        return "C"
    elif userscore < 90:
        return "B"
    elif userscore < 101:
        return "A"
    
main()
