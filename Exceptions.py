#age = int(input("Age: "))
#print(age)
    #the code above will give us a value error and crash the program if we input a letter or a word instead of a number because its integer 
    #this is where Exceptions come
try:
    age = int(input("Age: "))
    print(age)

except ValueError:
    print("Please enter a number")

#So now instead of crashing the program it will print an error message to the user 

print("""
      
now calculating income and risk
      
      """)

try:
    income=2000
    risk=0
    #this will give us ZeroDivisionError if we don't use Exception and crash the program
    print(f"income = {income} and risk = {risk} income/risk = {income/risk}")

except ZeroDivisionError:
    print(f"income = {income} and risk = {risk} income/risk = Erorr")
    print("you can't devide by zero")