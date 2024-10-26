# Chapter 8: Strings

# 8.1  A string is a sequence
def access_string_element():
    """
    Demonstrates how to access individual characters in a string.
    
    The function creates a string 'banana' and retrieves specific characters
    using index positions. Index in Python starts from 0.
    
    Returns:
        tuple: Contains the characters 'a' and 'b', retrieved from the string.
    """
    fruit = 'banana'
    letter_1 = fruit[1]  # Accessing the second character 'a' 
    letter_2 = fruit[0]  # Accessing the first character 'b'
    return letter_1, letter_2

result = access_string_element()
print(result)  #('a', 'b')

# We can also use an expression that contains variables and operators.
i = 2
letter = fruit[i]
print(letter)  #'n'

# The value of index has to be an integer.
print(fruit[1.5])  #TypeError: string indices must be integers


# 8.2  Len
# len is a built-in function that returns the number of characters in a string:
fruit = 'banana'
print(len(fruit))  #6 (The length of 'banana' is 6)

# To get the last letter of a string, should be:
def get_last_letter(fruit):
    """
    A function that gets the last character from a string.
    
    Param:
        fruit : The string from which the last character will be returned.
    
    Returns:
        str: The last character of the string.
    """
    length = len(fruit) # Calculate the length of the string
    last_letter = fruit[length - 1]  # Subtract 1 because index starts from 0
    return last_letter

print(get_last_letter('banana'))  #'a'
print(get_last_letter('apple'))  #'e'


# 8.3  Traversal with a for loop
# While loop
def traverse_with_while(fruit):
    """
    Traverse through each character in the string 'fruit' using a while loop.
    The 'while' loop starts with 'index' as 0 and continues until 'index' is less than the length of 'fruit'.
    In each iteration, the character at the current 'index' is stored in the variable 'letter' and printed.
    Then, 'index' is incremented by 1 to move to the next character in the string.
    The loop ends when all characters in the string have been printed.
    
    Param:
        fruit : The string to traverse through.
    """
    index = 0
    while index < len(fruit):
        letter = fruit[index]
        print(letter)
        index = index + 1

print(traverse_with_while('banana')) #b a  n  a  n  a (each on a new line)

# Exercise: Write a function that takes a string as an argument and displays the letters backward, one per line.
def word_backward(word):
    """
    A function that prints the characters of a string in reverse order, one character per line.
    The loop starts with 'index' as the last index of the string and continues until 'index' is greater than or equal to 0.
    In each iteration, the character at the current 'index' is stored in the variable 'letter' and printed.
    Then, 'index' is decremented by 1 to move to the previous character in the string.
    The loop ends when all characters in the string have been printed in reverse order.

    Param:
        word : The string to print in reverse order.

    """
    index = len(word) - 1
    while index >= 0:
        letter = word[index]
        print(letter)
        index = index - 1

print(word_backward('banana')) #a n a n a b (each on a new line)

# For loop
def traverse_with_for(fruit):
    """
    Traverse through each character in the string 'fruit' using a for loop.
    The 'for' loop iterates over each character in the string 'fruit' and assign it in the variable 'letter'.
    In each iteration, the character is printed.
    The loop ends when all characters in the string have been printed.
    
    Parameters:
    fruit : The string to traverse through.
    """
    for letter in fruit:
        print(letter)

print(traverse_with_for(blueberry)) #b l u e b e r r y (each on a new line)

# String concatenation
def names_with_prefixes(prefixes, suffix):
    """
    A function that prints a list of names by concatenating each letter from the 'prefixes' with 'suffix'.
    
    Parameters:
    prefixes : A string containing prefix letters.
    suffix : The suffix to append to each letter in the prefixes.
    """
    for letter in prefixes:
        print(letter + suffix)

print(names_with_prefixes('JKLMNOPQ', 'ack')) #Jack, Kack, Lack, Mack, Nack, Oack, Pack, Qack (each on a new line)

# Exercise: “Ouack” and “Quack” are misspelled. Modify the program to fix this error.
def names_with_prefixes(prefixes, suffix):
    """
    A function that prints a list of names by concatenating each letter from the 'prefixes' with 'suffix'.
    If the letter is 'O' or 'Q', the function concatenates 'u' with the letter and the suffix.

    Paremeters:
    prefixes : A string containing prefix letters.
    suffix : The suffix to append to each letter in the prefixes.
    """
    for letter in prefixes:
        if letter == 'O' or letter == 'Q':
            print(letter + 'u' + suffix)
        else:
            print(letter + suffix)

print(name_with_prefixes('JKLMNOPQ', 'ack')) #Jack, Kack, Lack, Mack, Nack, Ouack, Pack, Quack (each on a new line)


# 8.4 String slices
# String slices
s = 'Monty Python'
# An operator that returns string slicing in Python.
# Syntax [n:m], where 'n' is the index of the first character and 'm' is the end index, but the character at 'b' is not included.

print(s[0:5]) # Monty
print(s[6:12]) # Python
print(s[7:2]) # empty string 
print(s[3:3]) # empty string 

# If you omit the first index, the slice starts at the beginning of the string.
print(s[:2]) # Mo
print(s[8:]) # thon
print(s[:]) # Monty Python (copy of the whole string)


# 8.5 Strings are immutable
# Strings are immutable, which means that once a string is created, it cannot be changed. Will be error if we change it.
greeting = 'Hello, world!'
greeting[0] = 'J' # attemps to change the first character
# TypeError: 'str' object does not support item assignment

# If we want to change a string, we have to create a new string that is a variation of the original.
greeting = 'Hello, world!'
new_greeting = 'J' + greeting[1:] # Concatenate a new string with 'J' and the slice of the original string.
print(new_greeting) # Jello, world!

# 8.6 Searching
def find(word, letter):
    """
    A function that searches for the first occurrence of 'letter' in the string 'word'.
    The function starts by initializing index = 0 and loops through each character in the string word.
    If word[index] == letter, it returns the current index, stopping the loop immediately.
    If the loop completes and the character is not found, it returns -1, indicating that the letter was not present in the string.
    
    Param:
    word: The string to search through.
    letter: The character to find.
    
    Returns:
    int: The index of the first occurrence of 'letter', or -1 if not found.
    """
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index  # Return the index as soon as the letter is found
        index = index + 1
    return -1  # Return -1 if the letter is not found

print(find('hello', 'h')) # 0
print(find('hello', 'l')) # 2 (The second 'l' is at index 3, but the function returns the index of the first occurrence.)
print(find('hello', 'z')) # -1

# Exercise: Modify find so that it has a third parameter, the index in word where it should start searching.
def find(word, letter, start_index):
    """
    A function that searches for the first occurrence of 'letter' in the string 'word' starting from the 'start_index'.
    It takes a third parameter, 'start_index', which specifies the position in the string where the search should begin instead of '0'

    Param:
    word: The string to search through.
    letter: The character to find.
    start_index: The index in word where the search should start.
    
    Returns:
    int: The index of the first occurrence of 'letter', or -1 if not found.
    """
    index = start_index
    while index < len(word):
        if word[index] == letter:
            return index  # Return the index as soon as the letter is found
        index = index + 1
    return -1  # Return -1 if the letter is not found

print(find('hello', 'l', 2)) # 2
print(find('hello', 'l', 3)) # 3 
print(find('Programming', 'a', 3)) # 5
print(find('Programming', 'm', 6)) # 6

# 8.7 Looping and counting
def count_a_in_string(word):
    """
    A function that counts the number of times the letter 'a' appears in the given string 'word'.
    Variable 'count' is initialized to 0, and then incremented each time an a is found.
    When the loop exits, count contains the result—the total number of 'a'.
    
    Param:
    word: The string in which to count occurrences of 'a'.
    
    Returns:
    int: The count of 'a' in the string.
    """
    count = 0
    for letter in word:
        if letter == 'a':
            count = count + 1
    return count

word = 'banana'
print(count_a_in_string(word))  #3

# Exercise: Encapsulate this code in a function named count, and generalize it so that it accepts the string and the letter as arguments.
def count(word, letter):
    """
    A function that counts the number of times the specified 'letter' appears in the given string 'word'.
    Variable 'count' is initialized to 0, and then incremented each time the specified letter is found.
    When the loop exits, count contains the result—the total number of occurrences of the specified letter.

    Param:
    word: The string in which to count occurrences of 'letter'.
    letter: The character to count.

    Returns:
    int: The count of 'letter' in the string 'word'.
    """
    count = 0
    for char in word:
        if char == letter:
            count = count + 1
    return count

print(count('Python', 'a')) # 0
print(count('Python', 'n')) # 1

# 8.8 String Methods
def convert_to_uppercase(word):
    """
    A function that converts the given string 'word' to uppercase.
    Using the string method upper()
    The syntax word.upper() invokes the upper method on the string word.
    This syntax, using a dot (.), is called dot notation. The method name (upper) follows the object name (word), and empty parentheses () indicate that the method takes no arguments.


    Param:
    word (str): The string to be converted.
    
    Returns:
    str: The uppercase version of the string.
    """
    return word.upper()

print(convert_to_uppercase("banana"))  # 'BANANA'
print(convert_to_uppercase("Hello, World!"))  # 'HELLO, WORLD!'

