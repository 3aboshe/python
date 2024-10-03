# with a dictionary we can store key value pairs
customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
    #each key must be uniqe using for ex "age" again is forbidden
    
 }
print(customer["name"])

# we can also give a value to a non existing key 
print(customer.get("birthdate","1 Dec 1999"))

# we can also update the value
customer["name"]="Jack Smith"
print(customer["name"])

#we can also add a key value to a dictionary
customer["Gender"]= "male"
print(customer["Gender"])
