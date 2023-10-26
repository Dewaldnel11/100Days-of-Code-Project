print("Welcome to the tip calculator")
Bill = float(input("What was the total of the Bill ?"))
#print(Bill)
Tip_per = int(input("How much would you like to tip ? 10, 12, or 15"))
#print(Tip_per)
people = int(input("How many people to split the bill"))
Tip_per_person = (Bill/Tip_per*100)/people
print(Tip_per_person)
