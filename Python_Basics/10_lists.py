```python
# Lists in Python

# A list is a collection of multiple values.
# Lists are ordered and mutable.


# 1. Creating a list

fruits = ["apple", "banana", "orange"]

print(fruits)


# 2. A list can contain different types of values

student = ["Aarti", 29, "Data Analytics", True]

print(student)


# 3. Accessing list elements

fruits = ["apple", "banana", "orange"]

print(fruits[0])
print(fruits[1])
print(fruits[2])


# Python uses zero-based indexing.
# The first element has index 0.


# 4. Negative indexing

print(fruits[-1])
print(fruits[-2])


# 5. Changing a list element

fruits[1] = "mango"

print(fruits)


# 6. Adding an element using append()

fruits.append("grapes")

print(fruits)


# 7. Adding an element at a specific position

fruits.insert(1, "banana")

print(fruits)


# 8. Adding multiple elements using extend()

fruits.extend(["kiwi", "watermelon"])

print(fruits)


# 9. Removing an element

fruits.remove("mango")

print(fruits)


# 10. Removing an element using pop()

fruits.pop()

print(fruits)


# pop() can also remove an element using its index

fruits.pop(1)

print(fruits)


# 11. Finding the length of a list

numbers = [10, 20, 30, 40, 50]

print(len(numbers))


# 12. Checking whether an element exists

fruits = ["apple", "banana", "orange"]

print("apple" in fruits)
print("mango" in fruits)


# 13. Slicing a list

numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[:])


# 14. Sorting a list

numbers = [40, 10, 30, 20, 50]

numbers.sort()

print(numbers)


# Sorting in descending order

numbers.sort(reverse=True)

print(numbers)


# 15. Reversing a list

numbers.reverse()

print(numbers)


# 16. Finding minimum and maximum

numbers = [10, 20, 5, 40, 30]

print(min(numbers))
print(max(numbers))


# 17. Finding the sum

print(sum(numbers))


# 18. Looping through a list

fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(fruit)


# 19. Using a condition with a list

numbers = [10, 15, 20, 25, 30]

for number in numbers:

    if number > 20:
        print(number)


# 20. Nested list

students = [
    ["Aarti", 29],
    ["Rahul", 25],
    ["Priya", 27]
]

print(students[0])
print(students[0][0])
print(students[0][1])


# 21. List length

students = ["Aarti", "Rahul", "Priya"]

print(len(students))


# 22. Lists are mutable

numbers = [10, 20, 30]

numbers[0] = 100

print(numbers)

# The original list was changed.
# This is called mutability.
```

