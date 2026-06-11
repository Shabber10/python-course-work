# Day 7: Strings Part 1

Strings are sequences of characters enclosed in single or double quotes.

## String Indexing
Each character in a string has an index (position). Python supports positive (left-to-right) and negative (right-to-left) indexing.
- First character: index `0`
- Last character: index `-1`

```python
text = "Python"
print(text[0])  # 'P'
print(text[-1]) # 'n'
```

## String Slicing
Extracting a substring. Syntax: `string[start:stop:step]`
```python
text = "Programming"
print(text[0:4])   # 'Prog' (from index 0 up to, not including 4)
print(text[4:])    # 'ramming' (from index 4 to end)
print(text[:4])    # 'Prog' (from start up to 4)
print(text[::-1])  # 'gnimmargorP' (Reverses the string)
```

## String Concatenation & Repetition
```python
str1 = "Hello"
str2 = "World"

# Concatenation (+)
print(str1 + " " + str2)

# Repetition (*)
print(str1 * 3) # "HelloHelloHello"
```
