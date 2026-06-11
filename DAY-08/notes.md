# Day 8: Strings Part 2

Strings in Python are **immutable**, meaning they cannot be changed after they are created. String methods return new strings instead of modifying the original.

## Useful String Methods

```python
text = "  Hello Python  "

# Strip whitespace from ends
print(text.strip())

# Convert case
print(text.lower())
print(text.upper())

# Replace a substring
print(text.replace("Python", "World"))

# Split a string into a list
csv_data = "apple,banana,cherry"
fruits = csv_data.split(",") # ['apple', 'banana', 'cherry']
```

## Escape Characters
Used to insert characters that are illegal in a string.
- `\n`: Newline
- `\t`: Tab
- `\\`: Backslash
- `\'` or `\"`: Quotes

```python
print("Line 1\nLine 2")
```

## F-Strings (Formatted String Literals)
A cleaner way to format strings (available in Python 3.6+).
```python
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")
```
