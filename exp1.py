my_string = "Dinesh Ahire !" 
print(my_string[0])
print(my_string[7])
print(my_string[0:5])
greeting = "Hello" 
name = "John"
full_greeting = greeting + " " + name
print (full_greeting) 
age = 30
print (f"My name is {name} and I am {age} years old.")

#2 lists
my_list = ["apple", "banana","cherry"] 
print (my_list[0])
print(my_list[2])
print (my_list[0:2]) 
my_list.append("orange") 
print(my_list)
my_list.remove("banana")
print(my_list)

#3 dict
my_dict = {"name": "John","age": 30, "country": "USA"}
print (my_dict["name"])
print (my_dict["age"])
my_dict["city"] = "New York"
print (my_dict)
del my_dict ["country"] 
print (my_dict)
 

#tuples
my_tuple = ("apple", "banana","cherry")
print (my_tuple[0])
print (my_tuple[2]) 
print (my_tuple[0:2])
my_list = list (my_tuple) 
print (my_list)
