print("Welcome to the tip calculator")
Bill = float(input("What was the total of the Bill ?"))
#print(Bill)
Tip = int(input("How much would you like to tip ? 10, 12, or 15"))
#print(Tip_per)
people = int(input("How many people to split the bill"))
Bill_with_tip = Tip / 100 * Bill + Bill
Bill_per_person = Bill_with_tip / people
round(Bill_per_person,2)
print(Bill_per_person)
