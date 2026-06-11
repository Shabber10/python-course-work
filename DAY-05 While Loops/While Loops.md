# DAY-05 While Loops

Python has two primitive loop commands:
- `while` loops
- `for` loops

## 1. The `while` Loop
With the `while` loop we can execute a set of statements as long as a condition is true.
**Important:** Remember to increment `i`, or else the loop will continue forever (infinite loop).

**Input:**
```python
# Print i as long as i is less than 4:
i = 1
while i < 4:
    print(i)
    i += 1
```
**Output:**
```text
1
2
3
```

## 2. The `break` Statement
With the `break` statement we can stop the loop even if the while condition is true.

**Input:**
```python
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
```
**Output:**
```text
1
2
3
```

## 3. The `continue` Statement
With the `continue` statement we can stop the current iteration, and continue with the next.

**Input:**
```python
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)
```
**Output:**
```text
1
2
4
5
```
*(Notice that `3` is missing from the output)*

## 4. The `else` Statement
With the `else` statement we can run a block of code once when the condition no longer is true.

**Input:**
```python
i = 1
while i < 4:
    print(i)
    i += 1
else:
    print("i is no longer less than 4")
```
**Output:**
```text
1
2
3
i is no longer less than 4
```
