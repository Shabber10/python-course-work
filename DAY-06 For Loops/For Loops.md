# DAY-06 For Loops

A `for` loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
This is less like the `for` keyword in other programming languages, and works more like an iterator method.

## 1. Syntax and Basic Iteration
**Input:**
```python
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
```
**Output:**
```text
apple
banana
cherry
```

## 2. Looping Through a String
Strings are iterable objects, they contain a sequence of characters.
**Input:**
```python
for x in "banana":
    print(x)
```
**Output:**
```text
b
a
n
a
n
a
```

## 3. The `break` and `continue` Statements
`break` stops the loop completely, `continue` skips the current iteration and moves to the next.
**Input:**
```python
for x in ["apple", "banana", "cherry"]:
    if x == "banana":
        continue
    print(x)
```
**Output:**
```text
apple
cherry
```

## 4. The `range()` Function
To loop through a set of code a specified number of times, we can use the `range()` function.
- `range(stop)`
- `range(start, stop)`
- `range(start, stop, step)`

**Input:**
```python
# Range from 2 to 6 (exclusive of 6)
for x in range(2, 6):
    print(x)

# Range with step of 3
for y in range(2, 10, 3):
    print(f"y: {y}")
```
**Output:**
```text
2
3
4
5
y: 2
y: 5
y: 8
```

## 5. The `else` in For Loop
The `else` keyword in a `for` loop specifies a block of code to be executed when the loop is finished.
**Input:**
```python
for x in range(3):
    print(x)
else:
    print("Finally finished!")
```
**Output:**
```text
0
1
2
Finally finished!
```
*Note: The `else` block will NOT be executed if the loop is stopped by a `break` statement.*

## 6. Nested Loops
A nested loop is a loop inside a loop. The "inner loop" will be executed one time for each iteration of the "outer loop".
**Input:**
```python
adj = ["red", "big"]
fruits = ["apple", "cherry"]

for a in adj:
    for f in fruits:
        print(a, f)
```
**Output:**
```text
red apple
red cherry
big apple
big cherry
```

## 7. The `pass` Statement
`for` loops cannot be empty, but if you for some reason have a `for` loop with no content, put in the `pass` statement to avoid getting an error.
**Input:**
```python
for x in [0, 1, 2]:
    pass
print("Loop passed without errors.")
```
**Output:**
```text
Loop passed without errors.
```
