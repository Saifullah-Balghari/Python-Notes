from typing import List

list1 = ["Orange", "Banana", "Mango", "WaterMelon", "PineApple"]
print("Original")
print(list1)

list1.append("Apple")
print("Apple is added:")
print(list1)

list1.sort()
print("Sorted:")
print(list1)

list1.sort(reverse=True)
print("Reversed:")
print(list1)

first_element = list1[0]
print("first element:")
print(first_element)

index_of_Apple = list1.index('Apple')
print("index of Apple:")
print(index_of_Apple)

# etc
