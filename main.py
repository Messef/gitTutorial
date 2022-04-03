#WORDLE
from random import randint
wordle= [ "rebut","trope", "cobra", "adieu", "storm", "arise", "awake", "sleep", "snake", "couch", "chair", "phone"]
word=randint(0,12)
z=wordle[word]
counter=0
iterator=0
print("Welcome to Worldle! For each letter you guess it will throw a \"y\" or \"n\". An \"n\" means that for that for that specific letter in that word, the letter is incorrect. For example, if you guess \"phone\" and the word is \"trope\", the program will throw this: \n p, n \n h, n \n o, y \n n, n \n e, y \n Thus, despite there being an \"p\" in trope, the program isn't sophisticated enough to see that there is a p in the letter, just not in the position guessed. A \"y\" means that that letter is 100% right.  ")
def myFunc():
  
  global counter
  global iterator
  iterator=0
  while counter<5:
   guess=input("Put a five letter word here: ")
   guess=guess.lower()
   if len(guess)!=5:
    print("invalid guess, start again")
   else:
    def wordle():
     global counter
     global iterator
     while iterator<5:
      if z[iterator]==guess[iterator]:
        
        print(f"{guess[iterator]}, y")
        iterator+=1
        if iterator==4:
          if z[iterator]==guess[iterator]:
           print(f"{guess[iterator]}, y")
           myFunc()
           counter+=1
           iterator+=1
          elif z[iterator]!=guess[iterator]:
           print(f"{guess[iterator]}, n")
           myFunc()
           counter+=1
           iterator+=1
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
           myFunc()
          elif z[iterator]!=guess[iterator]:
           print(f"{guess[iterator]}, n")
           iterator+=1
           counter+=1
           myFunc()
        else:
          wordle()
    wordle()      
myFunc()