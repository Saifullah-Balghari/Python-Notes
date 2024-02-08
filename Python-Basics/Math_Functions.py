# Example usage of some math functions

# min() and max()
x = min(5, 10, 25)
y = max(5, 10, 25)
print("min:", x)
print("max:", y)

# abs()
z = abs(-7.25)
print("abs:", z)

# pow()
a = pow(2, 3)  # Equivalent to 2 ** 3
print("pow:", a)

# round()
b = round(3.75)
print("round:", b)

# sum()
c = sum([1, 2, 3, 4, 5])
print("sum:", c)

# divmod()
d = divmod(9, 2)
print("divmod:", d)  # Output: (4, 1), 9 divided by 2 gives quotient 4 and remainder 1

# pow() with three arguments
e = pow(2, 3, 5)  # Equivalent to (2 ** 3) % 5
print("pow with three args:", e)

# Other math functions are available in the math module
import math

# sqrt() from the math module
f = math.sqrt(64)
print("sqrt:", f)

# floor() from the math module
g = math.floor(3.75)
print("floor:", g)

# ceil() from the math module
h = math.ceil(3.75)
print("ceil:", h)
