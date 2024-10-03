guess=8
tries=0

while tries <3:
     win= input("Guess: ")
     if   win == "8":
          print("You Guessed Right!")
          break;
     tries = 1+ tries
     if tries == 3:
          print("You are out of tries try again later")

     