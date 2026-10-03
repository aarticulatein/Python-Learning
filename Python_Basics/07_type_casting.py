```python
# Type Casting in Python

# Type casting means converting a value from one data type to another data type.


# 1. Integer to Float

age = 29

age_float = float(age)

print(age_float)
print(type(age_float))


# 2. Integer to String

number = 100

number_string = str(number)

print(number_string)
print(type(number_string))


# 3. Float to Integer

price = 19.99

price_integer = int(price)

print(price_integer)
print(type(price_integer))

# The decimal part is removed.
# It is not rounded.


# 4. String to Integer

number = "25"

number_integer = int(number)

print(number_integer)
print(type(number_integer))


# 5. String to Float

price = "19.99"

price_float = float(price)

print(price_float)
print(type(price_float))


# 6. Integer to Boolean

number = 1

print(bool(number))

print(bool(0))
print(bool(10))

# 0 becomes False.
# Any non-zero number becomes True.


# 7. String to Boolean

text = ""

print(bool(text))

text = "Python"

print(bool(text))

# An empty string becomes False.
# A non-empty string becomes True.


# 8. Type Casting with input()

# input() always returns a string.

age = input("Enter your age: ")

print(age)
print(type(age))


# Convert input from string to integer

age = int(input("Enter your age: "))

print(age)
print(type(age))


# 9. Type Casting for calculations

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

print(number1 + number2)
```
