```python
# String Methods in Python

# A string is a sequence of characters.


# 1. Changing letter case

text = "hello python"

print(text.upper())       # HELLO PYTHON
print(text.lower())       # hello python
print(text.capitalize())  # Hello python
print(text.title())      # Hello Python


# 2. Removing whitespace

text = "   Aarti Sharma   "

print(text.strip())   # Removes whitespace from both ends
print(text.lstrip())  # Removes whitespace from the left
print(text.rstrip())  # Removes whitespace from the right


# 3. Replacing text

text = "I am learning Java"

new_text = text.replace("Java", "Python")

print(new_text)


# 4. Finding the length of a string

text = "Python"

print(len(text))


# 5. Counting occurrences

text = "banana"

print(text.count("a"))
print(text.count("an"))


# 6. Finding a substring

text = "I am learning Python"

print(text.find("Python"))
print(text.find("Java"))

# find() returns -1 if the substring is not found.


# 7. Checking the beginning and ending

filename = "sales.csv"

print(filename.startswith("sales"))
print(filename.endswith(".csv"))


# 8. Checking string contents

text = "Python"

print(text.isalpha())

number = "12345"

print(number.isdigit())

text = "Python123"

print(text.isalnum())


# 9. Splitting a string

text = "Python,SQL,Power BI"

skills = text.split(",")

print(skills)


# 10. Joining strings

skills = ["Python", "SQL", "Power BI"]

text = ", ".join(skills)

print(text)


# 11. Checking whether text exists

text = "I am learning Python"

print("Python" in text)
print("Java" in text)


# 12. Removing a prefix or suffix

filename = "report_2026.csv"

print(filename.removesuffix(".csv"))
print(filename.removeprefix("report_"))


# 13. String indexing

text = "Python"

print(text[0])
print(text[-1])


# 14. String slicing

text = "Python"

print(text[0:3])
print(text[2:])
print(text[:4])


# 15. Strings are immutable

text = "python"

# text[0] = "P"  # Raises TypeError

text = "P" + text[1:]

print(text)


# 16. Practical example: cleaning a name

name = "   AARTI SHARMA   "

clean_name = name.strip().title()

print(clean_name)


# 17. Practical example: standardising categories

category = "  ELECTRONICS  "

clean_category = category.strip().lower()

print(clean_category)


# 18. Practical example: cleaning a phone number

phone = "123-456-7890"

clean_phone = phone.replace("-", "")

print(clean_phone)
```
