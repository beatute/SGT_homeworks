# Task 1: Find the max of three numbers:

def numbers(*value):
    return max(value)

print(numbers(7,77,79))


# Task 2: Reverse a string:

def given_string(text):
    return text [::-1]

reverse_string = given_string("123456asdfdfvd")
print(reverse_string)

# Task 3: Write a function to calculate the sum of all numbers passed as its arguments:

def sum_numbers(*numbers):
    """Sum numbers"""
    return sum(numbers)

print(sum_numbers(1, 2, 3))
print(sum_numbers(8, 20, 2))
print(sum_numbers(12.5, 3.147, 98.1))
print(sum_numbers(1.1, 2.2, 5.5))



import time
time.sleep(5)
