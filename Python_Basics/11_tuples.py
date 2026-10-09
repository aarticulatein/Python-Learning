```python
# Tuples in Python

# A tuple is a collection of multiple values.
# Tuples are ordered and immutable.


# 1. Creating a tuple

fruits = ("apple", "banana", "orange")

print(fruits)


# 2. A tuple can contain different types of values

student = ("Aarti", 29, "Data Analytics", True)

print(student)


# 3. Accessing tuple elements

fruits = ("apple", "banana", "orange")

print(fruits[0])
print(fruits[1])
print(fruits[2])


# Python uses zero-based indexing.


# 4. Negative indexing

print(fruits[-1])
print(fruits[-2])


# 5. Tuple slicing

numbers = (10, 20, 30, 40, 50)

print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[:])


# 6. Finding the length of a tuple

numbers = (10, 20, 30, 40, 50)

print(len(numbers))


# 7. Checking whether an element exists

fruits = ("apple", "banana", "orange")

print("apple" in fruits)
print("mango" in fruits)


# 8. Looping through a tuple

fruits = ("apple", "banana", "orange")

for fruit in fruits:
    print(fruit)


# 9. Tuple methods

numbers = (10, 20, 20, 30, 40)

# count() tells us how many times a value appears

print(numbers.count(20))


# index() tells us the position of a value

print(numbers.index(30))


# 10. Finding minimum and maximum

numbers = (10, 20, 5, 40, 30)

print(min(numbers))
print(max(numbers))


# 11. Finding the sum

print(sum(numbers))


# 12. Tuple unpacking

student = ("Aarti", 29, "Data Analytics")

name, age, course = student

print(name)
print(age)
print(course)


# 13. Tuple with one element

number = (10,)

print(number)
print(type(number))


# The comma is important.
# Without the comma, it is just an integer.

number = (10)

print(type(number))


# 14. Tuples are immutable

numbers = (10, 20, 30)

# numbers[0] = 100
# This will produce a TypeError because
# tuple elements cannot be changed.


# 15. Converting a list to a tuple

numbers_list = [10, 20, 30]

numbers_tuple = tuple(numbers_list)

print(numbers_tuple)
print(type(numbers_tuple))


# 16. Converting a tuple to a list

numbers_tuple = (10, 20, 30)

numbers_list = list(numbers_tuple)

print(numbers_list)
print(type(numbers_list))
```
