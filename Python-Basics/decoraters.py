
import time
import math
 
def calculate_time(func):
     
    def inner1(*args):
 
        begin = time.time()
         
        func(*args)
        end = time.time()
        print("Total time taken in : ", func.__name__, end - begin)
    return inner1
 
@calculate_time
def factorial(num):
 
    print(math.factorial(num))
 
factorial(5)