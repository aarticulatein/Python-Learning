```python
# Operators in Python


# 1. Arithmetic Operators
# Used to perform mathematical calculations

a = 10
b = 3

print(a + b)   # Addition
print(a - b)   # Subtraction
print(a * b)   # Multiplication
print(a / b)   # Division
print(a // b)  # Floor division
print(a % b)   # Modulus (remainder)
print(a ** b)  # Exponentiation


# 2. Assignment Operators
# Used to assign or update values in variables

x = 10

x += 5
print(x)

x -= 3
print(x)

x *= 2
print(x)

x /= 4
print(x)


# 3. Comparison Operators
# Compare two values and return True or False

a = 10
b = 20

print(a == b)   # Equal to
print(a != b)   # Not equal to
print(a > b)    # Greater than
print(a < b)    # Less than
print(a >= b)   # Greater than or equal to
print(a <= b)   # Less than or equal to


# 4. Logical Operators
# Used to combine conditions

age = 25

print(age > 18 and age < 30)
print(age < 18 or age > 60)
print(not age < 18)


# 5. Membership Operators
# Check whether a value exists in a sequence

name = "Aarti"

print("A" in name)
print("z" in name)

print("A" not in name)


# Membership operators with a list

courses = ["Python", "SQL", "Power BI"]

print("Python" in courses)
print("Excel" in courses)


# 6. Identity Operators
# Check whether two variables refer to the same object

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)
print(a is c)

print(a is not c)
```
