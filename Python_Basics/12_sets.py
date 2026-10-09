```python
# Sets in Python

# A set is a collection of unique elements.
# Sets are mutable and do not support indexing.


# 1. Creating a set

fruits = {"apple", "banana", "orange"}

print(fruits)


# 2. Sets automatically remove duplicates

numbers = {10, 20, 10, 30, 20, 40}

print(numbers)


# 3. Creating an empty set

empty_set = set()

print(empty_set)
print(type(empty_set))

# {} creates an empty dictionary, not an empty set.


# 4. Adding an element

fruits = {"apple", "banana", "orange"}

fruits.add("mango")

print(fruits)


# 5. Adding multiple elements

fruits.update(["grapes", "kiwi"])

print(fruits)


# 6. Removing an element using remove()

fruits.remove("banana")

print(fruits)

# remove() raises KeyError if the element does not exist.


# 7. Removing an element using discard()

fruits.discard("watermelon")

print(fruits)

# discard() does not raise an error if the element is missing.


# 8. Removing an arbitrary element using pop()

fruits = {"apple", "banana", "orange"}

removed_fruit = fruits.pop()

print(removed_fruit)
print(fruits)

# Do not rely on which element pop() removes.


# 9. Removing all elements

fruits.clear()

print(fruits)


# 10. Checking whether an element exists

fruits = {"apple", "banana", "orange"}

print("apple" in fruits)
print("mango" in fruits)


# 11. Looping through a set

for fruit in fruits:
    print(fruit)

# Sets do not guarantee a particular iteration order.


# 12. Union: elements from both sets

set_a = {1, 2, 3}
set_b = {3, 4, 5}

print(set_a.union(set_b))
print(set_a | set_b)


# 13. Intersection: common elements

print(set_a.intersection(set_b))
print(set_a & set_b)


# 14. Difference: elements in the first set but not the second

print(set_a.difference(set_b))
print(set_a - set_b)


# 15. Symmetric difference: elements in either set, but not both

print(set_a.symmetric_difference(set_b))
print(set_a ^ set_b)


# 16. Checking subsets and supersets

small_set = {1, 2}
large_set = {1, 2, 3, 4}

print(small_set.issubset(large_set))
print(large_set.issuperset(small_set))


# 17. Removing duplicates from a list

numbers = [10, 20, 10, 30, 20, 40]

unique_numbers = set(numbers)

print(unique_numbers)

# Note: converting back to a set does not preserve list order.


# 18. Finding unique values in two groups

sql_students = {"Aarti", "Rahul", "Priya"}
python_students = {"Aarti", "Priya", "Neha"}

print("Students learning either subject:")
print(sql_students | python_students)

print("Students learning both subjects:")
print(sql_students & python_students)

print("Students learning SQL but not Python:")
print(sql_students - python_students)
```
