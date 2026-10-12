```python
# Error Handling in Python

# Error handling allows us to manage errors using try, except, else, and finally.


# 1. A simple try-except block

try:
    print(10 / 0)

except ZeroDivisionError:
    print("A number cannot be divided by zero.")


# 2. Handling invalid input

try:
    age = int(input("Enter your age: "))
    print(age)

except ValueError:
    print("Please enter a valid whole number.")


# 3. Handling different types of errors

try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(result)

except ValueError:
    print("Invalid input. Please enter a number.")

except ZeroDivisionError:
    print("The number cannot be zero.")


# 4. Using else

# else executes if no exception occurs.

try:
    number = int(input("Enter a number: "))

except ValueError:
    print("Invalid input.")

else:
    print("Your number is:", number)


# 5. Using finally

# finally executes whether an exception occurs or not.

try:
    number = int(input("Enter a number: "))
    print(number)

except ValueError:
    print("Invalid input.")

finally:
    print("Program execution completed.")


# 6. Storing the error message

try:
    number = int("hello")

except ValueError as error:
    print("Error:", error)


# 7. Handling an error when accessing a list

numbers = [10, 20, 30]

try:
    print(numbers[5])

except IndexError:
    print("The requested index does not exist.")


# 8. Handling a missing dictionary key

student = {"name": "Aarti"}

try:
    print(student["age"])

except KeyError:
    print("The requested key does not exist.")


# 9. Handling file errors

try:
    with open("data.csv", "r", encoding="utf-8") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("The file was not found.")


# 10. Raising an exception manually

age = -5

try:
    if age < 0:
        raise ValueError("Age cannot be negative.")

except ValueError as error:
    print(error)


# 11. Using try-except-else-finally together

try:
    number = int(input("Enter a number: "))
    result = 100 / number

except ValueError:
    print("Please enter a valid integer.")

except ZeroDivisionError:
    print("Zero is not allowed.")

else:
    print("Result:", result)

finally:
    print("Calculation finished.")


# 12. Practical example: converting data safely

values = ["10", "20", "abc", "30", "xyz"]

valid_numbers = []

for value in values:
    try:
        number = int(value)

    except ValueError:
        print("Skipping invalid value:", value)

    else:
        valid_numbers.append(number)

print("Valid numbers:", valid_numbers)
```
