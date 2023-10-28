print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L") 
add_pepperoni = input("Do you want pepperoni? Y or N") 
extra_cheese = input("Do you want extra cheese? Y or N") 

Bill = 0
if size == "S":
  Bill += 15
elif size == "M":
  Bill +=20
else:
  Bill += 25

if add_pepperoni == "Y":
  if size == "S":
    Bill += 2
  else:
    Bill += 3

if extra_cheese == "Y":
  Bill += 1

print(f"Your final bill is: ${Bill}.")