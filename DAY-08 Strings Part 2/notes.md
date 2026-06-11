# Day 8: Strings Part 2 (Built-in Functions)

Strings in Python are **immutable**, meaning they cannot be changed after they are created. String methods return new strings instead of modifying the original.

Here is a well-organized list of built-in string functions.

---

## 1. Case Manipulation

### `upper()`
Converts all characters in the string to uppercase.
**Input:**
```python
text = "hello world"
print(text.upper())
```
**Output:**
```text
HELLO WORLD
```

### `lower()`
Converts all characters in the string to lowercase.
**Input:**
```python
text = "PYTHON"
print(text.lower())
```
**Output:**
```text
python
```

### `capitalize()`
Capitalizes the first letter of the string.
**Input:**
```python
text = "hello world"
print(text.capitalize())
```
**Output:**
```text
Hello world
```

---

## 2. Trimming / Stripping Whitespace

### `strip()`
Removes leading (beginning) and trailing (end) whitespace.
**Input:**
```python
text = "   too much space   "
print(text.strip())
```
**Output:**
```text
too much space
```

---

## 3. Splitting and Joining

### `split()`
Splits a string into a list based on a specified separator (default is whitespace).
**Input:**
```python
csv_data = "apple,banana,cherry"
print(csv_data.split(","))
```
**Output:**
```text
['apple', 'banana', 'cherry']
```

### `join()`
Joins a list of strings into a single string using a specified separator.
**Input:**
```python
fruits_list = ['apple', 'banana', 'cherry']
print(" | ".join(fruits_list))
```
**Output:**
```text
apple | banana | cherry
```

---

## 4. Searching and Replacing

### `find()`
Returns the lowest index of a substring. Returns `-1` if not found.
**Input:**
```python
sentence = "The quick brown fox"
print(sentence.find("fox"))
```
**Output:**
```text
16
```

### `replace()`
Replaces all occurrences of a specified substring with another string.
**Input:**
```python
greeting = "Hello, World!"
print(greeting.replace("World", "Python"))
```
**Output:**
```text
Hello, Python!
```

---

## 5. Checking String Content

### `isdigit()`
Returns True if all characters in the string are digits.
**Input:**
```python
number_str = "12345"
print(number_str.isdigit())
```
**Output:**
```text
True
```

### `isalpha()`
Returns True if all characters in the string are letters.
**Input:**
```python
word = "Python123"
print(word.isalpha())
```
**Output:**
```text
False
```
