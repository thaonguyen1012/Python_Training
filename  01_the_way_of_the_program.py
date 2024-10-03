# Chapter 1: The way of the program
print("Hello World!")

# Arithmetic operators
print(40 + 5) # 45
print(40 - 5) # 35
print(40 * 2) # 80
print(40 / 2) # 20
# a**b = a^b
print(5**2 - 5) 
# a ^ b (XOR - Bitwise operator)
print(5 ^ 2) # 5 XOR 2 = 7 (bitwise operation)
print(5 % 2) # 5 mod 2 = 1 (returns the remainder of the division)

# Values and types
print(type(5)) # int (interger)
print(type(5.0)) # float (floating point number)
print(type('Hello Thao')) # str (string)
print(type('45')) #str
#print(type(2,000,000)) # error: not a legal interger in Python

print(type(2000000))  # int
# Using underscores as separators for readability
print(type(2_000_000))  # int

#Ex1: 
#print("Hello World!" 
#1. In a print statement, what happens if you leave out one of the parentheses, or both? => SyntaxError 
#print('Python learning)
#2. If you are trying to print a string, what happens if you leave out one of the quotation marks, or both? => IndentationError: unexpected indent
#print(2++2)
#3. You can use a minus sign to make a negative number like -2. What happens if you put a plus sign before a number? What about 2++2? => = 4 (because Python evaluates the expression 2++2 = 2 + (+2))
#print(09)
#print(011)
#4. In math notation, leading zeros are ok, as in 09. What happens if you try this in Python? What about 011? => SyntaxError
#4 8
#5. What happens if you have two values with no operator between them?
# => SyntaxError: invalid syntax (because Python requires an operator between values)
#print(2 2)

#Ex2: 
#1. How many seconds are there in 42 minutes 42 seconds?
print(42 * 60 + 42) #2562s
#2. How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.
print(10 / 1.61) #6.21
#3. If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace (time per mile in minutes and seconds)? What is your average speed in miles per hour?
print(2562 / 6.21) # 413.56 (s/mile)
print(2562 / 60 / 6.21) #6.88 (m/mile)
print(6.21 / (2562 / 60**2)) #8.73 (miles/h)



