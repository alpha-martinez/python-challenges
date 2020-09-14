# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

def add_numbers(num1, num2):
    result = num1 + num2
    return result

def subtract_numbers(num1, num2):
    result = num1 - num2
    return result

def multiply_numbers(num1, num2):
    result = num1 * num2
    return result

def divide_numbers(num1, num2):
    result = num1 / num2
    return result  


calc = input('What calculation would you like to do? (add, sub, mult, div)')
num1 = int(input("1st number?"))
num2 = int(input("2nd Number?"))

if calc == "add":
    print(add_numbers)