# DAY-07 Strings Part 1

Strings in Python are surrounded by either single quotation marks, or double quotation marks. `'hello'` is the same as `"hello"`.

## 1. String Literals
**Input:**
```python
print("Hello")
print('Hello')
```
**Output:**
```text
Hello
Hello
```

## 2. Multiline Strings
You can assign a multiline string to a variable by using three quotes (single `'''` or double `"""`).
**Input:**
```python
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit."""
print(a)
```
**Output:**
```text
Lorem ipsum dolor sit amet,
consectetur adipiscing elit.
```

## 3. Strings are Arrays
Like many other popular programming languages, strings in Python are arrays of bytes representing Unicode characters. However, Python does not have a character data type, a single character is simply a string with a length of 1.
Square brackets can be used to access elements of the string.
**Input:**
```python
a = "Hello, World!"
print(a[1]) # Index 1 is the 2nd character
```
**Output:**
```text
e
```

## 4. Looping Through a String
Since strings are arrays, we can loop through the characters in a string, with a `for` loop.
**Input:**
```python
for x in "cat":
    print(x)
```
**Output:**
```text
c
a
t
```

## 5. String Length
To get the length of a string, use the `len()` function.
**Input:**
```python
a = "Hello, World!"
print(len(a))
```
**Output:**
```text
13
```

## 6. Check String (`in`, `not in`)
To check if a certain phrase or character is present in a string, we can use the keyword `in`.
**Input:**
```python
txt = "The best things in life are free!"
print("free" in txt)
print("expensive" not in txt)
```
**Output:**
```text
True
True
```

## 7. String Slicing
You can return a range of characters by using the slice syntax. Specify the start index and the end index, separated by a colon, to return a part of the string.
- `[start:stop:step]`

**Input:**
```python
b = "Hello, World!"
print(b[2:5])   # Positive Slicing: From index 2 to 5 (not included)
print(b[:5])    # Slice From the Start
print(b[7:])    # Slice To the End
print(b[-5:-2]) # Negative Slicing: Use negative indexes to start the slice from the end of the string
```
**Output:**
```text
llo
Hello
World
orl
```
