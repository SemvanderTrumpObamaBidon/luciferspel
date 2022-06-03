print("Welcome by Lucifer!")
def game():
  print()
  naam = input("Please enter your name:\n")

  question = input ("Would you like to play this game? type yes or no\n")
  if question == "yes":
    print("Nice! Lets get started")
  elif question == "no":
    print("Are you sure? lets try this again!") 
    game()
game()











