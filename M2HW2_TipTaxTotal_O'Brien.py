# CTI-110 
# M2HW2 - Tip Tax Total 
# Anthony
# 09/07/2017

subtotal = float(input("Total?: "))
tax = subtotal * .07
tip = .18 * subtotal
total = subtotal + tax + tip
print("Total with tax and tip:$", total)
tipamount = tip - subtotal
print("Tip amount:$", tip)
print("Tax amount:$", tax)
