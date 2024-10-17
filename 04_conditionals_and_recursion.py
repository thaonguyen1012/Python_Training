# Chapter 5: Conditionals and recursion

# 5.1  Floor division and modulus
minutes = 105
hours = minutes // 60  # Floor division
print(hours)  # 1
minutes = minutes % 60  # Modulus
print(minutes)  # 45

# Check if a number is divisible by another
number = 20
print(number % 2 == 0)  # True

# 5.2  Boolean expressions
print(5 == 5)  # True, because 5 equals 5
print(5 == 6) # False, because 5 does not equal 6
print(type(True))   # <class 'bool'>
print(type(False))  # <class 'bool'>

# relational operators
print(5 != 6)  # True,
print(5 < 6)  # True,
print(5 > 6)  # False,
print(5 <= 6)  # True
print(5 >= 6)  # False

# 5.3  Logical operators
x = 5
print(x > 0 and x < 10) #True , both conditions are true

n = 6
print(n % 2 == 0 or n % 3 == 0)  # True, because 6 is divisible by both 2 and 3

y = 5
print(not (y > 10))  # True, because x > 10 is false

# 5.4  Conditional execution
x = 10

if x % 2 == 0:
    print('x is even')
else:
    print('x is odd')
# x is even

# 5.5  Alternatice execution
x = 5
if x % 2 == 0:
    print('x is even')  # This will run if x is divisible by 2
else:
    print('x is odd')  # This will run if x is not divisible by 2
# x is odd

# 5.6  Chained conditionals
x = 5
y = 10

if x < y:
    print('x is less than y')  # This runs if x is less than y
elif x > y:
    print('x is greater than y')  # This runs if x is greater than y
else:
    print('x and y are equal')  # This runs if x is equal to y
# x is less than y

# 5.7  Nested conditionals
x = 10
y = 10

if x == y:
    print('x and y are equal')
else:
    if x < y:
        print('x is less than y')
    else:
        print('x is greater than y')
# x and y are equal

# 5.8  Recursion (Đệ quy)
def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1)

countdown(10)
#10
#9
#8
#7
#6
#5
#4
#3
#2
#1
#Blastoff!

def print_n(s, n):
    if n <= 0:
        return
    print(s)
    print_n(s, n-1)

print_n('Python', 5)
#Python
#Python
#Python
#Python
#Python

# 5.9 Stack diagrams for recursive functions
# 5.10 Infinite recursion
def recurse():
    recurse()
    # This function calls itself, causing an infinite loop

recurse()
# RecursionError: maximum recursion depth exceeded

# 5.11 Keyboard input