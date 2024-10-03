choice2 = ""
strcount =0
stpcount = ""
while choice2 != "quit":
    choice2 = input(">")
    if choice2 == "quit":
        break
    elif choice2 == "help":
        print("""
            start - to start the car
            stop - to stop the car
            quit - to exit""")
    elif choice2 == "start":
        
        if strcount == 0:
            print("Car is started Ready to go")
        else:
            print("the car has already started")
        strcount = 1 + strcount
        stpcount = 0 
    elif choice2 == "stop":
        
        if stpcount == 0:
            print("the Car has stopped")
        elif strcount == 0:
            print("Bruh u can't stop a car that's not started")
        else:
            print("the car has already stopped")
        stpcount = 1 + stpcount
        strcount = 0
    else :
        print("invalid input please type help to see commands")