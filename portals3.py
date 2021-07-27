print()
print()
print()
solo = input("How many players are playing  ")
try:
  if int(solo) == 1:
    solo = "alone"
    print(solo)
  elif int(solo) == 2:
    solo = "duo"
    print(solo)
  elif int(solo) >= 3:
    print("we can only attend 2 players max right now")
except ValueError:
   print("Please enter a numerical value")



