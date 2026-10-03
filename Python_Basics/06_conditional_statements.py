```python
# Conditional Statements in Python


# 1. if statement
# The code inside if runs only when the condition is True

age = 20

if age >= 18:
    print("You are an adult.")


# 2. if-else statement
# else runs when the if condition is False

age = 16

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")


# 3. if-elif-else statement
# Used when there are multiple conditions

marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Grade D")


# 4. Multiple conditions using logical operators

age = 25

if age >= 18 and age <= 30:
    print("Age is between 18 and 30.")


# 5. Using or

day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("It is the weekend.")


# 6. Nested if statement
# An if statement inside another if statement

age = 25
has_id = True

if age >= 18:
    print("Age requirement is satisfied.")

    if has_id:
        print("You can enter.")
    else:
        print("ID is required.")
else:
    print("You are not old enough.")


# 7. Checking positive, negative, or zero

number = 10

if number > 0:
    print("Positive number")
elif number < 0:
    print("Negative number")
else:
    print("Zero")


# 8. Checking whether a number is even or odd

number = 7

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# 9. Taking input and using a condition

age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")


# 10. Conditional expression (ternary operator)

age = 20

result = "Adult" if age >= 18 else "Minor"

print(result)
```
