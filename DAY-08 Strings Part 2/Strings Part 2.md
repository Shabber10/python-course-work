# DAY-08 Strings Part 2 (Modifying and Methods)

Python has a set of built-in methods that you can use on strings. All string methods return new values. They do not change the original string.

## 1. Modifying Strings (Case and Trimming)

### `upper()` & `lower()`
**Input:**
```python
a = "Hello, World!"
print(a.upper())
print(a.lower())
```
**Output:**
```text
HELLO, WORLD!
hello, world!
```

### `strip()`
Removes whitespace from the beginning and the end.
**Input:**
```python
a = " Hello, World! "
print(a.strip())
```
**Output:**
```text
Hello, World!
```

## 2. Replacing and Splitting

### `replace()`
Replaces a string with another string.
**Input:**
```python
a = "Hello, World!"
print(a.replace("H", "J"))
```
**Output:**
```text
Jello, World!
```

### `split()`
Splits the string into substrings if it finds instances of the separator.
**Input:**
```python
a = "Hello, World!"
print(a.split(","))
```
**Output:**
```text
['Hello', ' World!']
```

## 3. String Concatenation
To concatenate, or combine, two strings you can use the `+` operator.
**Input:**
```python
a = "Hello"
b = "World"
c = a + " " + b
print(c)
```
**Output:**
```text
Hello World
```

## 4. String Formatting
As we learned in the Python Variables chapter, we cannot combine strings and numbers directly with `+`. Instead, we format them.

### F-Strings (Python 3.6+)
**Input:**
```python
age = 36
txt = f"My name is John, I am {age}"
print(txt)
```
**Output:**
```text
My name is John, I am 36
```

### `.format()` Method
**Input:**
```python
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
```
**Output:**
```text
I want 3 pieces of item 567 for 49.95 dollars.
```

## 5. Escape Characters
To insert characters that are illegal in a string, use an escape character `\`.
- `\'` Single Quote
- `\\` Backslash
- `\n` New Line
- `\t` Tab

**Input:**
```python
txt = "We are the so-called \"Vikings\" from the north.\nNew Line."
print(txt)
```
**Output:**
```text
We are the so-called "Vikings" from the north.
New Line.
```

## 6. Boolean String Methods (Checking Content)

### `isalpha()`, `isdigit()`, `isalnum()`
**Input:**
```python
print("Python".isalpha())    # Only letters
print("123".isdigit())       # Only numbers
print("Python123".isalnum()) # Letters and numbers
```
**Output:**
```text
True
True
True
```
