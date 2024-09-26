# Chapter 2: Variables, expression and statements

message = 'Im sitting in front of computer and reading a Python book'  # Assign a string value to 'message'
n = 20  # Assign an integer to 'n'
pi = 3.1415926535897932  # Assign a approximate value to 'pi'


#variable names can contain both letters and numbers, but they can’t begin with a number. It is legal to use uppercase letters, but it is conventional to use only lower case for variables names.

# Correct syntax:
my_name = "Thao Nguyen"  
my_age_now = 24

# SyntaxError: invalid syntax examples: 
# 76trombones = 'big parade' (Variable cannot start with a number)
# more@ = 1000000  ('@' is an illegal character)

50  # This is a valid expression
n  # A variable can be an expression
n + 25  # An expression combining a variable and value but not print

n = 48  # Assignment statement
print(n)  #  48

miles = 25.5
print(miles * 1.61)  # Converts miles to kilometers (41.055)

# Order of Operations (PEMDAS)**
# Like in math, Python follows **PEMDAS** (Parentheses, Exponentiation, Multiplication/Division, Addition/Subtraction):

first_name = 'Vu'
last_name = 'Nguyen'
print(first_name + last_name)  # Concatenate two strings (VuNguyen)

print('Spam' * 5)  # Repetition of string (SpamSpamSpamSpamSpam)

#Ex 2.1
#42 = n #SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='? (Because the left-hand side of an assignment statement must be a variable, not a literal value)

x = y = 1 #legal
print(x,y) #1 1
n = 50; #legal
print(n) 

x = 5
y = 4
#print(xy) #NameError: name 'xy' is not defined
print(x * y) #20

#Ex 2.2
#2.2.1
radius = 5
volume = (4 / 3) * 3.14 * radius**3
print(volume) #523.3333333333334

#2.2.2
cover_price = 24.95
#discount = 40% #SyntaxError: invalid syntax
discount = 0.4
discounted_cover_price = cover_price * (1 - discount)
shipping_cost = 3 + 0.75 * 59
copies = 60

total_cost = discounted_cover_price * copies + shipping_cost
print(total_cost) # 945.45 

#2.2.3