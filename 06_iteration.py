# Chapter 7  Iteration

## 7.1 Reassignment
# In python, we can assign a value to a variable and then change that value later. It's legal
x = 5
print(x) # 5
x = 10
print(x) # 10

# In this example, when a is updated to 3, b is not updated, and it still keep the first value is 5 because assigment is not the same as equality.
a = 5
b = a # a and b are now equal
a = 3 # a and b are no longer equal
print(a) # 3
print(b) # 5

## 7.2 Updating Variables
x = x + 1 # NameError: name 'x' is not defined

# increment (+ 1)
x = 1
x = x + 1
print(x) # 2

# decrement (- 1)
x = 5
x = x - 1
print(x) # 4

## 7.3 The while statement
def countdown(n):
    while n > 0:
        print(n)
        n = n - 1
    print('Blastoff!')

print(countdown(3)) # 3 2 1 Blastoff!

def sequence(n):
    while n != 1:
        print(n)
        if n % 2 == 0:        # n is even
            n = n / 2
        else:                 # n is odd
            n = n*3 + 1

print(sequence(3)) # 3 10 5.0 16.0 8.0 4.0 2.0 None
print(sequence(5)) # 5 16 8.0 4.0 2.0 None

## 7.4 Break
while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)

print('Done!')
# This loop will continue to prompt the user for input until they type 'done'.

## 7.5 Square roots
# Newton's method for square roots
a = 4
x = 3
y = (x + a / x) / 2
print(y) # 2.1666666666666665

# if repeat the process with the new estimate, the result is even closer to the correct answer
x = y
y = (x + a / x) / 2
print(y) # 2.0064102564102564

# using loop to repeat the calculation
while True:
    print(x)
    y = (x + a / x) / 2
    if y == x:
        break
    x = y

# its better to use the build-in function abs to compute the absolute value of the difference between x and y
while True:
    print(x)
    y = (x + a / x) / 2
    if abs(y-x) < epsilon: # epsilon has value 0.0000001 
        break
    x = y

## 7.6 Algorithms
## 7.7 Debugging
# 1. Make sure that the loop is executing the body of the loop.
# 2. Make sure that the test expression in the header of the loop is true the first time the loop is executed.
# 3. Make sure that the loop is exited when it is appropriate.
# 4. Make sure that the loop variables are updated correctly.

## 7.8 Glossary
## 7.9 Exercises
# 7.9.1
def mysqrt(a):
    while True:
      print(x)
      y = (x + a / x) / 2
      if abs(y-x) < epsilon: # epsilon has value 0.0000001 
          break
      x = y
    return x

