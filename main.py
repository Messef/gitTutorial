#WORDLE
from random import randint
wordle= [ "rebut","trope", "cobra", "adieu", "storm", "arise", "awake", "sleep", "snake", "couch", "chair", "phone", "maker", "whale", "fifth", "twice", "leave", "patio"]
word=randint(0,17)
z=wordle[word]
counter=0
iterator=0
letterRight=0
print("Welcome to Wordle! For each letter you guess it will throw a \"y\" or \"n\". An \"n\" means that for that for that specific letter in that word, the letter is incorrect. For example, if you guess \"phone\" and the word is \"trope\", the program will throw this: \n p, n \n h, n \n o, y \n n, n \n e, y \n Thus, despite there being an \"p\" in trope, the program isn't sophisticated enough to see that there is a p in the letter, just not in the position guessed. A \"y\" means that that letter is 100% right.  ")
def myFunc():
  global letterRight
  global counter
  global iterator
  letterRight=0
  iterator=0
  while counter<7:
   guess=input("Put a five letter word here: ")
   guess=guess.lower()
   if len(guess)!=5:
    print("invalid guess, start again")
   else:
    def wordle():
     global letterRight
     global counter
     global iterator
     while iterator<5:
      if z[iterator]==guess[iterator]:
        letterRight+=1
        print(f"{guess[iterator]}, y")
        iterator+=1
        if iterator==4:
          if z[iterator]==guess[iterator]:
           print(f"{guess[iterator]}, y")
           letterRight+=1
           if letterRight==5:
             print("Congrats!")
             counter+=1
             iterator+=1
             print(counter)
             quit()
           else:
            myFunc()
            counter+=1
            iterator+=1
            print(counter)
          elif z[iterator]!=guess[iterator]:
           print(f"{guess[iterator]}, n")
           myFunc()
           counter+=1
           iterator+=1
           print(counter)
        else:
          wordle()
      elif z[iterator]!=guess[iterator]:
        print(f"{guess[iterator]}, n")
        iterator+=1
        if iterator==4:
          if z[iterator]==guess[iterator]:
           print(f"{guess[iterator]}, y")
           iterator+=1
           counter+=1
           print(counter)
           myFunc()
          elif z[iterator]!=guess[iterator]:
           print(f"{guess[iterator]}, n")
           iterator+=1
           counter+=1
           print(counter)
           myFunc()
        else:
          wordle()
    wordle()   
  else:
     print(z)
     quit()
myFunc()