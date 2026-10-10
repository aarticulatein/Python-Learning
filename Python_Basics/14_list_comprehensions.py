```python
# List Comprehensions in Python

# List comprehension provides a concise way to create a new list from an iterable, such as a list, range, or string.


# 1. Creating a list using a for loop

numbers = [1, 2, 3, 4, 5]

squares = []

for number in numbers:
    squares.append(number ** 2)

print(squares)


# 2. Creating the same list using list comprehension

numbers = [1, 2, 3, 4, 5]

squares = [number ** 2 for number in numbers]

print(squares)


# Syntax:
# [expression for item in iterable]


# 3. Creating a list of numbers using range()

numbers = [number for number in range(1, 6)]

print(numbers)


# 4. Squaring numbers

squares = [number ** 2 for number in range(1, 6)]

print(squares)


# 5. Converting strings to uppercase

names = ["aarti", "rahul", "priya"]

uppercase_names = [name.upper() for name in names]

print(uppercase_names)


# 6. Extracting even numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = [number for number in numbers if number % 2 == 0]

print(even_numbers)


# Syntax with a condition:
# [expression for item in iterable if condition]


# 7. Extracting odd numbers

odd_numbers = [number for number in numbers if number % 2 != 0]

print(odd_numbers)


# 8. Filtering numbers greater than 5

numbers = [2, 5, 7, 9, 3, 10]

large_numbers = [number for number in numbers if number > 5]

print(large_numbers)


# 9. Using if-else in a list comprehension

numbers = [1, 2, 3, 4, 5, 6]

results = [
    "Even" if number % 2 == 0 else "Odd"
    for number in numbers
]

print(results)

# Syntax:
# [value_if_true if condition else value_if_false for item in iterable]


# 10. Converting strings to integers

numbers = ["10", "20", "30", "40"]

integer_numbers = [int(number) for number in numbers]

print(integer_numbers)


# 11. Extracting the length of each string

names = ["Aarti", "Rahul", "Priya"]

name_lengths = [len(name) for name in names]

print(name_lengths)


# 12. Removing whitespace from strings

names = [" Aarti ", " Rahul ", " Priya "]

clean_names = [name.strip() for name in names]

print(clean_names)


# 13. Filtering strings by length

names = ["Aarti", "Raj", "Priya", "Aman"]

long_names = [name for name in names if len(name) > 4]

print(long_names)


# 14. Working with a string

text = "Python"

letters = [letter for letter in text]

print(letters)


# 15. Nested list comprehension

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

flattened = [number for row in matrix for number in row]

print(flattened)


# 16. List comprehension with multiple conditions

numbers = range(1, 21)

results = [
    number
    for number in numbers
    if number % 2 == 0 and number > 10
]

print(results)


# 17. Practical example: filtering sales

sales = [50, 150, 200, 75, 300, 90]

high_sales = [sale for sale in sales if sale > 100]

print(high_sales)


# 18. Practical example: calculating revenue

quantities = [2, 3, 4, 5]
unit_prices = [10, 20, 15, 8]

revenue = [
    quantity * price
    for quantity, price in zip(quantities, unit_prices)
]

print(revenue)
```
