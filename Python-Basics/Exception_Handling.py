try:
  num = int(input("Enter an integer: "))
  a = [6, 3, 4, 4, 2, 5, 7, 1, 4]
  print(a[num])
except ValueError:
  print("Number entered is not an integer.")

except IndexError:
   print("Index error!")
  
# finally:
#     print("I am always executed")

number = int(input("Enter any number: "))

if number > 100:
  raise Exception("greater then 100")