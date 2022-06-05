
import random

"""
eisen game:
V Er wordt gebruik gemaakt van commentaar in het programma.
V Er wordt minimaal 1 functie gebruikt.
V Er is input van de gebruiker (evt. met controle op de invoer).
X Er wordt gebruik gemaakt van concatenation. (MENEER WAT WILT U VAN ONS??????????) 
V Er wordt gebruik gemaakt van string methodes.
V Er wordt gebruik gemaakt van tenminste één while-loop.
V (bij verbeteringen) Er wordt gebruik gemaakt van een list.
 
"""
#concatenation hebben wij er niet in want wij gebruiken een f string ipv de concatenation.
intro_game="""

 _              _    ___               
| |            (_)  / __)              
| | _   _  ____ _ _| |__ _____  ____   
| || | | |/ ___) (_   __) ___ |/ ___)  
| || |_| ( (___| | | |  | ____| |      
 \_)____/ \____)_| |_|  |_____)_|      
                                       
                                       
                                       
      ____ _____ ____  _____           
     / _  (____ |    \| ___ |          
    ( (_| / ___ | | | | ____|          
     \___ \_____|_|_|_|_____)          
    (_____|                            


"""
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
#geeft aantal lucifers gekozen door computer 
def bepaal_aantal_lucifers(): 
  aantalLucifers = random.randint(20,25)
  print(f"de computer heeft {aantalLucifers} lucifers gekozen")
  return aantalLucifers
  
#speler kiest aantal lucifers volgens spel regels
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

#compuer kiest aantal lucifers volgens de regels
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

#hoe het spel zelf werkt, functie roept zichzelf aan
def game(beurt):
  global aantalLucifers
  print()

  #computer en speler spelen om de beurt, speler begint
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

    nog_een_keer=input("wil je nog een keer spelen? type yes/no\n")
    if nog_een_keer == "yes": 
      aantalLucifers = bepaal_aantal_lucifers()
      game(1)
    else: 
      print("oke doei")

# Laat de intro van de game zien en geeft de naam van de speler terug
def intro():
  print(intro_game)
  print(" Welkom bij de lucifer game, het spel is easyy. De computer kiest een willekeurig aantal lucifers tussen de 20 en 25. jij  als eerste de keuze om 1, 2 of 3 lucifers weg te nemen. Daarna is het de beurt van de computer. De computer neemt ook 1, 2 of 3 lucifers weg. Dit gaat door totdat iemand als laatste een lucifer MOET wegnemen. als je de laatste hebt wegnomen heb je verloren moet de computer dit doen dan heb jij gewonnen")
  return input ("Wat is je naam?\n")
      
#intro en game worden gestart
naam = intro()
aantalLucifers = bepaal_aantal_lucifers()
game(1)












