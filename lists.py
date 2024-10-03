numbers = [1,2,3,4,4,5,5,6,6]
x = 0
count = numbers.count(x)
for item in numbers:
    if numbers.count(x) == 2 :
     
     numbers.remove(x)

    x += 1
print (numbers)