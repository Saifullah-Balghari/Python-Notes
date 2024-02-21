# M A P

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
map_list = list(map(lambda x: x*x, list1))
print(map_list)

# F I L T E R

list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
filter_list = list(filter(lambda x: x>5, list2))
print(filter_list)

# R E D U C E
from functools import reduce

list3 = [5, 4, 3, 2, 1]
recuced_list = [reduce(lambda x,y: x*y, list3)]
print(recuced_list)
