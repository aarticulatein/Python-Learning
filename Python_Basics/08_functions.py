```python
# Functions in Python

# A function is a reusable block of code that performs a specific task.


# 1. Creating a simple function

def greet():
    print("Hello, Aarti!")


# Calling the function

greet()


# 2. Function with a parameter

def greet_person(name):
    print("Hello,", name)


greet_person("Aarti")
greet_person("Rahul")


# 3. Function with multiple parameters

def add_numbers(a, b):
    print(a + b)


add_numbers(10, 20)
add_numbers(5, 15)


# 4. Returning a value from a function

def add_numbers(a, b):
    return a + b


result = add_numbers(10, 20)

print(result)


# A returned value can be stored in a variable

total = add_numbers(5, 7)

print(total)


# 5. Difference between print() and return

def multiply_print(a, b):
    print(a * b)


def multiply_return(a, b):
    return a * b


multiply_print(5, 4)

result = multiply_return(5, 4)

print(result)


# 6. Using the returned value in another calculation

def square(number):
    return number * number


result = square(5)

print(result)
print(result + 10)


# 7. Default parameter

def greet(name="Aarti"):
    print("Hello,", name)


greet()
greet("Rahul")


# 8. Keyword arguments

def student_info(name, age, course):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)


student_info(
    name="Aarti",
    age=29,
    course="Data Analytics"
)


# 9. Multiple parameters and return value

def calculate_total(price, quantity):
    total = price * quantity
    return total


total = calculate_total(25, 4)

print(total)


# 10. Function with a condition

def check_age(age):

    if age >= 18:
        return "Adult"
    else:
        return "Minor"


result = check_age(25)

print(result)


# 11. A function can return multiple values

def calculate(a, b):

    addition = a + b
    subtraction = a - b

    return addition, subtraction


result1, result2 = calculate(20, 10)

print(result1)
print(result2)


# 12. Local variable

def calculate_square(number):

    result = number * number

    return result


answer = calculate_square(6)

print(answer)

# result exists only inside the function.
# Variables created inside a function are local variables.


# 13. Function documentation using a docstring

def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    """
    return length * width


area = calculate_area(10, 5)

print(area)
```
