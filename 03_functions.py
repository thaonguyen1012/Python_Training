# Chapter 3: Functions

## 3.1 Function calls
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
