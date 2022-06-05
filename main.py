import random

game_over_tekst = """

  ________                       
 /  _____/_____    _____   ____  
/   \  ___\__  \  /     \_/ __ \ 
\    \_\  \/ __ \|  Y Y  \  ___/ 
 \______  (____  /__|_|  /\___  >
        \/     \/      \/     \/ 
                                 
     _______  __ ___________     
    /  _ \  \/ // __ \_  __ \    
   (  <_> )   /\  ___/|  | \/    
    \____/ \_/  \___  >__|       
                    \/           

"""
you_won="""

                    .-'''-.                       
                   '   _    \                     
                 /   /` '.   \                    
 .-.          .-.   |     \  '                    
  \ \        / /|   '      |  '                   
   \ \      / / \    \     / /                    
    \ \    / /   `.   ` ..' /_    _               
     \ \  / /       '-...-'`| '  / |              
      \ `  /               .' | .' |              
       \  /                /  | /  |              
       / /                |   `'.  |              
   |`-' /         .-'''-. '   .'|  '/       ___   
    '..'         '   _    \`-'  `--'     .'/   \  
               /   /` '.   \    _..._   / /     \ 
       _     _.   |     \  '  .'     '. | |     | 
 /\    \\   //|   '      |  '.   .-.   .| |     | 
 `\\  //\\ // \    \     / / |  '   '  ||/`.   .' 
   \`//  \'/   `.   ` ..' /  |  |   |  | `.|   |  
    \|   |/       '-...-'`   |  |   |  |  ||___|  
     '                       |  |   |  |  |/___/  
                             |  |   |  |  .'.--.  
                             |  |   |  | | |    | 
                             |  |   |  | \_\    / 
                             '--'   '--'  `''--'  

"""
def intro():
  naam = input ("Hoi, wat is je naam?\n")
  aantalLucifers = 2#random.randint(20,25)
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

def computer():
  if aantalLucifers <= 3:
    print("De computer lacht je uit want hij gaat winnen.")
    return aantalLucifers
  else:
    while True:
      x = random.randint(1,3)
      if x <= aantalLucifers:
        print(f"De computer neemt {x} lucifer weg")
        return x

def game(beurt):
  global aantalLucifers
  print()

  if beurt % 2 == 1:
    x = speler()
  else: 
    x = computer()
   
  aantalLucifers = aantalLucifers - x
  print(f"Nog {aantalLucifers} lucifers over")  

  if aantalLucifers > 0:
    game(beurt + 1)
  else:
    if beurt % 2 == 1:
      print(you_won)
    else: 
      print(game_over_tekst)

naam, aantalLucifers = intro()
game(1)












