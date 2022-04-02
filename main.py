from random import randint
class Dice:
  def __init__(self, sides):
    self.sides=sides
  def roll(self):
    z=input("Play? ")
    while z=="yes" or z=="Yes":
     y=input("Pick the number of sides: ")
     self.sides=y
     x=randint(1,int(self.sides))
     print("The dices says " + str(x) +"! The number of sides is " + str(y))
     z=input("Continue? ")
    else:
     quit()
counter=0
total=0
class Dice1(Dice):
  def __init__(dice):
   dice.target=randint(5, 15)
  def game(dice):
     global counter
     global total
     x=int(input("Pick a number from 1-5: "))
     if x!=1 and x!=2 and x!=3 and x!=4 and x!=5:
        quit()
     elif counter==2:
         total=total+x
         if total>dice.target:
          print("You lost")
          print(5)   
          print(total)
          print(dice.target)
         elif total<dice.target:
          score=dice.target-total
          print(score)
          print(4)
          print(dice.target)
     else:
        total=total+x
        counter=counter+1
        print(3)
        print(total)
        print(counter)
        Dice1.game(dice)
me=Dice1()
me.game()