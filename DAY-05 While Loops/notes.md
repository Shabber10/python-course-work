# Day 5: While Loops

Loops are used to execute a block of code repeatedly.

## `while` Loop
A `while` loop executes as long as a specified condition is `True`.

```python
# Print numbers from 1 to 5
count = 1
while count <= 5:
    print(count)
    count += 1  # Important: modify the loop control variable to avoid infinite loops!
```

## Infinite Loops
If the condition never becomes `False`, the loop runs forever.
```python
# while True:
#     print("This will run forever unless stopped manually.")
```

## `break` Statement in `while` loops
Used to exit the loop immediately, regardless of the condition.
```python
n = 1
while n <= 10:
    if n == 5:
        break # Exits the loop when n is 5
    print(n)
    n += 1
```

## `continue` Statement in `while` loops
Skips the current iteration and moves to the next iteration of the loop.
```python
m = 0
while m < 5:
    m += 1
    if m == 3:
        continue # Skips printing 3
    print(m)
```
