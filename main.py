import random

naam = ""
aantalLucifers = random.randint(20,25)
print(f"de computer heeft {aantalLucifers} lucifers gekozen")

def game():
  global aantalLucifers
  print()

  x = ""
  while x not in["1", "2", "3"]:
    x = input ("Hoeveel lucifers wil je weghalen? kies tussen 1,2 of 3 \n")

  aantalLucifers = aantalLucifers - int(x)
  print(f"Nog {aantalLucifers} lucifers over")  

  if aantalLucifers > 0:
    game()
  else:
    print("GAME OVER!")

game()












