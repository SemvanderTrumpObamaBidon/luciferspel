import random

def intro():
  naam = input ("Hoi, wat is je naam?\n")
  aantalLucifers = random.randint(20,25)
  print(f"de computer heeft {aantalLucifers} lucifers gekozen")
  return naam, aantalLucifers
  
def speler():
  x = ""
  while True:
    x = input (f"Hoeveel lucifers wil je weghalen {naam}? kies tussen 1,2 of 3 \n")

    if x in ["1", "2", "3"]:
      x = int(x)
      if x <= aantalLucifers:
        return x
      else:
        print("Je kunt niet meer lucifers weghalen dan die er zijn, sukkel....")

def game():
  global aantalLucifers
  print()

  x = speler()

  aantalLucifers = aantalLucifers - x
  print(f"Nog {aantalLucifers} lucifers over")  

  if aantalLucifers > 0:
    game()
  else:
    print("GAME OVER!")

naam, aantalLucifers = intro()
game()












