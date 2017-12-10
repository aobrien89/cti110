# CTI-110 
# M5T2 - Bug Collector
# Anthony O'Brien
# 10/22/2017

total = 0
for day in range(1, 8):
    print("Enter the bugs collected on day", day)
    bugs = int(input())
    total += bugs

print("You collected a total of", total, "bugs.") 
