weight = int(input("Enter your weight : "))
choice = input("(L)for pound (K)for kilo: ")
if choice == "L" or choice=="l":
    converted = weight/2.2
    print(f"Your weight in kilos is : {converted}")
elif choice == "K" or choice=="k":
    hello= weight * 2.2
    print(f"Your weight in pounds is : {hello}")
else :
    print("Incorrect Input Try Again Later")