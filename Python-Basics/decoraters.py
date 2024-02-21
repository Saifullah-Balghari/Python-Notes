import time
import math

num = int(input("Enter a number: "))

def start_end(func):

    def wrapper(*args, **kwargs):
        print("_____The program has started_____")    
        t1 = time.time()
        result = func(*args, **kwargs)
        time.sleep(1)
        print(f"Answer is {result}")
        t2 = time.time()
        t = t2 - t1
        print(f"The program took {t}")
        print("______The program has ended______")
        return result
    
    return wrapper

@start_end
def factorial(num):
    return math.factorial(num)

factorial(num)