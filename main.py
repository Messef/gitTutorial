#VIDEO GAME
import random
print("Ok, here are the things you need to do before you start playing:")
print("1.) Get a sibling or friend to this computer")
print("2.) Get a score sheet")
print("Ok, here are the rules:")
print("You and your friend will try to guess a random number between 1 and 10 and  enter it into the program. Whoever is closest wins! If you two are equally  as close then you will enter a tiebreaker round. If that is tied then you   tie the match!")

def theGame():
 score1=0
 score2=0
 x=int(random.randrange(1,10))
 you = float(input("Player 1, enter a number 1-10 here: "))
 other = float(input("Player 2, enter a number 1-10 here: "))
 if other==you:
   other=str(input("That number was taken! Please enter the word, \"Restart\" to restart: "))
   if other == "Restart" or other =="\"Restart\"":
     theGame()
 productv1 = abs(int(you)-x)
 productv2 = abs(int(other)-x)
 if productv1<productv2:
  x=input("Player 1 Won! The number was " + str(x) + ". Type \"Again\" to play again: ")
  score1=score1+1
  if x == "Again" or x == "\"Again\"" or x == "again":
    theGame()
 elif productv2<productv1:
  score2=score2+1
  x=input("Player 2 Won! The number was " + str(x) + ". Type \"Again\" to play again: ")
  if x == "Again" or x == "\"Again\"" or x == "again":
    theGame()
  elif x=="Leaderboard":
    x=input("Player one has " + str(score1) + " points, and Player2 has " + str(score2) + " points. Type \"Again\" to play again:")
    if x == "Again" or x == "\"Again\"" or x == "again":
     theGame()

theGame()
