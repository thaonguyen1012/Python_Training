# Chapter 3: Functions

## 3.1 Function calls
# define a function
def say_hi(): # function definition name: say_hi
    print('Hi') # function body

# call the function
say_hi()

type(42)
print(type(42)) 
# <class 'int'>

print(int('45'))
# 45

int('Hello World')
# ValueError: invalid literal for int() with base 11: 'Hello World'

# int can convert floating-point values to integers, but it doesn’t round, it cuts off the fractional part.
print(int(3.99999))
# 3

print(int(-2.5))
# -2

# float can convert integers and strings to floating-point numbers.
print(float(35))
# 35.0
print(float('3.12345'))
# 3.12345

# str can convert any value to a string.
print(str(2000))
# '2000'
print(str(1.23459))
# '1.23459'

## 3.2 Math functions
import math
print(math.sqrt(9))
# 3.0
print(math.sqrt(2) / 2.0)
# 0.7071067811865476
print(math.pi)
# 3.141592653589793
print(math.radiants(90))
# 1.5707963267948966 (degress to radians)
print(math.cos(0))
# 1.0

## 3.3 Composition
import math
x = math.sin(80 / 360.0 * 2 * math.pi)
print(x)
#0.984807753012208

## 3.4 Adding new functions
# define a function
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")

print_lyrics()

type(print_lyrics)

#Once we have defined a function, we can use it inside another function.
def repeat_lyrics():
    print_lyrics()
    print_lyrics()
    
repeat_lyrics()    

## 3.5 Definitions and uses
#Exercise: move 'repeat_lyrics' to the top and call it at the bottom. There will be 4 lines of error messages.
#ERROR!
#Traceback (most recent call last):
#  File "<main.py>", line 1, in <module>
#NameError: name 'repeat_lyrics' is not defined
repeat_lyrics()

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

# move the function call back to the bottom. Now the program will run sucessfully.
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

repeat_lyrics()

## 3.6 Flow of execution

def a():
    print("A is called")
    b()  # call function b from within function a
    print("A is finished")

def b():
    print("B is called")
    c()  # call function c from within function b
    print("B is finished")

def c():
    print("C is called")
    print("C is finished")

a()
#A is called
#B is called
#C is called
#C is finished
#B is finished
#A is finished

## 3.7 Parameters and arguments
def print_twice(bruce):
    print(bruce)
    print(bruce)

print_twice('programiz')
print_twice('programiz ' * 5)

import math
print_twice(math.cos(math.pi))

n = 10
print_twice(n)

print_twice('Spam ' * n)

## 3.8 Variables and parameters are local
def cat_twice(part1, part2):
    cat = part1 + part2
    print_twice(cat)
    
line1 = 'Bing tiddle '
line2 = 'tiddle bang.'
cat_twice(line1, line2) #print twice 'Bing tiddle tiddle bang.'
print(cat) #NameError: name 'cat' is not defined

## 3.9 Stack diagrams
## 3.10 Fruitful functions and void functions
#frutiful functions return a result
x = math.cos(radians)
golden = (math.sqrt(5) + 1) / 2

#void functions don't return a result
#print_twice is void function
result = print_twice('Bing')
print(result) #None