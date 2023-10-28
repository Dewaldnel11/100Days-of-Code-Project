weight = int(input("Enter your weight in kilograms e.g., 72"))
height = float(input("Enter your height in meters e.g., 1.55"))
BMI = weight / (height*height)

if BMI <18.5:
  print(f"Your BMI is {BMI}, you are underweight.")
elif BMI < 25:
  print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI <30:
  print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI <35:
  print(f"Your BMI is {BMI}, you are obese.")
else:
  print(f"Your BMI is {BMI}, you are clinically obese.")