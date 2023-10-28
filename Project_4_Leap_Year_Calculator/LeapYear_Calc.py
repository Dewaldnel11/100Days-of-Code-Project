#year = int(input("Please input year here ie. 1977: "))
#if year % 4 == 0:
 # print("Leap year")
#elif year % 100 >= 1:
#  print("Not leap year")
#elif year % 400 == 0:
#  print("Leap year")
#else:
 # print("lol")
year = int(input("Please input year here ie. 1977: "))
if year % 4 == 0:
  if year % 100 == 0:
      if year % 400 == 0:
        print("Leap year")
      else:
        print("Not leap year")
  else:
    print("Leap year")
else:
  print("Not leap year")


