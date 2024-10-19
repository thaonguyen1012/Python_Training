# Chapter 6: Fruitful Functions

#6.1 Return values
#esier to debug with a temporary variable (optional)
import math
def area(radius):
    temp = math.pi * radius**2
    return temp # return statement ends function execution and "returns" the result of the expression that follows.

def area(radius):
    return math.pi * radius**2

print(area(5))

def absolute_value(x):
    if x < 0:
        return -x
    else:
        return x
    # if x is 0, the function ends and returns 0
    

def absolute_value(x):
    if x < 0:
        return -x
    if x > 0:
        return x

print(absolute_value(0)) # none, because the function does not handle the case when x = 0

#exercise 6.1
def compare(x,y):
    if x > y:
        return 1
    if x == y:
        return 0
    if x < y:
        return -1

print(compare(20,10))

#6.2 Incremental development
def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = math.sqrt(dsquared)
    return result

# excercise 6.2
import math

def hypotenuse(a,b):
    h1 = a**2
    h2 = b**2
    csquared = h1 + h2
    result = math.sqrt(csquared)
    return result
    
print(hypotenuse(3,4)) # 5.0

#def hypotenuse(a,b):
#    h = math.sqrt(a**2 + b**2)
#    return h
    
#print(hypotenuse(3,4))

#6.3 Composition
def circle_area(xc, yc, xp, yp):
    radius = distance(xc, yc, xp, yp)
    result = area(radius)
    return result

#consise
def circle_area(xc, yc, xp, yp):
    return area(distance(xc, yc, xp, yp))

#6.4 Boolean functions
def is_divisible(x, y):
    if x % y == 0:
        return True
    else:
        return False
    
#consise
def is_divisible(x, y):
    return x % y == 0

if is_divisible(20, 5):
    print('x is divisible by y')

print(is_divisible(20, 5)) # x is divisible by y True
print(is_divisible(20, 6)) # False

#exercise 6.4
def is_between(x, y, z):
    if x <= y <= z:
        return True
    else:
        return False

#consise
def is_between(x, y, z):
    return x <= y <= z

print(is_between(1,2,3)) # True
print(is_between(1,3,2)) # False

#6.5 More recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result

print(factorial(5)) # 120
print(factorial(10)) # 3628800
print(factorial(0)) # 1

#6.6 Leap of faith
#6.7 One more example
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(10)) # 55
print(fibonacci(5)) # 5

#6.8 Checking types
# add type checking to make sure the arguments are of the right type
def factorial(n):
    if not isinstance(n, int):
        print('Factorial is only defined for integers.')
        return None
    elif n < 0:
        print('Factorial is not defined for negative integers.')
        return None
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial('1.5')) # Factorial is only defined for integers. None
print(factorial(-5)) # Factorial is not defined for negative integers. None
print(factorial('hello python')) # Factorial is only defined for integers. None
print(factorial(5)) # 120

#6.9 Debugging
def factorial(n):
    space = ' ' * (4 * n)
    print(space, 'factorial', n)
    if n == 0:
        print(space, 'returning 1')
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        print(space, 'returning', result)
        return result

print(factorial(3))
#             factorial 3
#         factorial 2
#     factorial 1
# factorial 0
# returning 1
#     returning 1
#         returning 2
#             returning 6
#6

#6.10 Glossary
#6.11 Exercises
def b(z):
    prod = a(z, z)
    print(z, prod)
    return prod

def a(x, y):
    x = x + 1
    return x * y

def c(x, y, z):
    total = x + y + z
    square = b(total)**2
    return square

x = 1
y = x + 1
print(c(x, y+3, x+y))
# 9 90
# 8100