# Day 6: For Loops

## `for` Loop
Used to iterate over a sequence (like a string, list, tuple, or a range of numbers).

## Using `range()`
The `range()` function generates a sequence of numbers.
`range(start, stop, step)`
- `start`: Starting number (inclusive, default is 0)
- `stop`: Ending number (exclusive)
- `step`: Increment (default is 1)

```python
# Print 0 to 4
for i in range(5):
    print(i)

# Print 2 to 6
for i in range(2, 7):
    print(i)

# Print even numbers from 2 to 10
for i in range(2, 11, 2):
    print(i)
```

## Iterating over Strings
You can loop through each character in a string.
```python
word = "Python"
for char in word:
    print(char)
```

## `pass` Statement
The `pass` statement is a null operation. It is used as a placeholder when a statement is required syntactically, but you don't want any code to execute.
```python
for i in range(5):
    if i == 3:
        pass # To be implemented later
    print(i)
```
