```python
# Dictionaries in Python

# A dictionary stores information as key-value pairs.
# Dictionaries are mutable.
# Keys must be unique.


# 1. Creating a dictionary

student = {
    "name": "Aarti Sharma",
    "age": 29,
    "course": "Data Analytics"
}

print(student)


# 2. Accessing values using keys

print(student["name"])
print(student["age"])
print(student["course"])


# 3. Using get() to access a value

print(student.get("name"))
print(student.get("grade"))

# get() returns None if the key does not exist.
# It does not raise a KeyError.


# 4. Adding a new key-value pair

student["city"] = "Berlin"

print(student)


# 5. Updating an existing value

student["age"] = 30

print(student)


# 6. Updating multiple values

student.update({
    "age": 29,
    "city": "Hamburg"
})

print(student)


# 7. Removing an item using pop()

student.pop("city")

print(student)


# 8. Removing the last inserted item using popitem()

student.popitem()

print(student)


# 9. Removing an item using del

del student["age"]

print(student)


# 10. Removing all items

student.clear()

print(student)


# 11. Getting all keys

student = {
    "name": "Aarti",
    "age": 29,
    "course": "Data Analytics"
}

print(student.keys())


# 12. Getting all values

print(student.values())


# 13. Getting all key-value pairs

print(student.items())


# 14. Looping through dictionary keys

for key in student:
    print(key)


# 15. Looping through dictionary values

for value in student.values():
    print(value)


# 16. Looping through keys and values

for key, value in student.items():
    print(key, ":", value)


# 17. Checking whether a key exists

print("name" in student)
print("grade" in student)


# 18. Finding the number of items

print(len(student))


# 19. A dictionary can contain different data types

employee = {
    "name": "Aarti",
    "age": 29,
    "salary": 45000.50,
    "is_active": True
}

print(employee)


# 20. A dictionary can contain a list

employee = {
    "name": "Aarti",
    "skills": ["Python", "SQL", "Power BI"]
}

print(employee["skills"])
print(employee["skills"][0])


# 21. Nested dictionaries

employees = {
    "employee_1": {
        "name": "Aarti",
        "department": "Analytics"
    },
    "employee_2": {
        "name": "Rahul",
        "department": "Finance"
    }
}

print(employees["employee_1"])
print(employees["employee_1"]["name"])


# 22. Creating a dictionary using dict()

student = dict(name="Aarti", age=29, course="Data Analytics")

print(student)


# 23. Creating a dictionary from two lists

keys = ["name", "age", "city"]
values = ["Aarti", 29, "Berlin"]

student = dict(zip(keys, values))

print(student)


# 24. Setting a default value using setdefault()

student = {"name": "Aarti"}

student.setdefault("course", "Data Analytics")
student.setdefault("name", "Rahul")

print(student)

# setdefault() adds the key only if it does not already exist.


# 25. Dictionary comprehension

numbers = [1, 2, 3, 4, 5]

squares = {number: number ** 2 for number in numbers}

print(squares)
```
