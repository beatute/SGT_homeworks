# Task 1: numbers from 0 to 100 divisible by 7:
numbers = [*range(0, 100)]
divisible_numbers_by_7 = []
for number in numbers:
    if number % 7 == 0:
        divisible_numbers_by_7.append(number)
print(divisible_numbers_by_7)

# Task 2: reverse a word with input function:

word = str(input("Please enter a word to reverse: "))

for letter in range(len(word) -1, -1, -1):
    print(word[letter], end="")
print("\n")


# Task 3: factorial function:

def factorial_function(number):
    if number == 1:
        return 1
    else:
        return (number * factorial_function(number-1))

number=int(input("Enter the number to calculate its factorial: "))
print(factorial_function(number))

