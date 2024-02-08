# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

list1 = ["apple", "Orange", "Banana", "Mango", "WaterMelon", "PineApple"]
set1 = {"apple", "Orange", "Banana", "Mango", "WaterMelon", "PineApple"}
tuple1 = ("apple", "Orange", "Banana", "Mango", "WaterMelon", "PineApple")
dictionary1 = {"brand": "Ford", "electric": False, "year": 1964, "colors": ["red", "white", "blue"]}

print(type(list1))
print(type(set1))
print(type(tuple1))
print(type(dictionary1), "\n")

print("This is list :", list1)
print("This is set :", set1)
print("This is tuple :", tuple1)
print("This is dictionary :", dictionary1)