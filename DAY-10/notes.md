# Day 10: Lists Part 2

## Advanced List Methods

```python
numbers = [3, 1, 4, 1, 5, 9, 2]

# sort() - Sorts the list ascending (modifies the original list)
numbers.sort()
# To sort descending:
numbers.sort(reverse=True)

# reverse() - Reverses the order of the list
numbers.reverse()

# count() - Returns the number of elements with the specified value
print(numbers.count(1))

# index() - Returns the index of the first element with the specified value
print(numbers.index(5))
```

## Nested Lists
Lists can contain other lists.
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Accessing '5'
print(matrix[1][1])
```

## List Comprehension
A concise way to create lists based on existing lists.
`[expression for item in iterable if condition == True]`

```python
# Create a list of squares from 1 to 5
squares = [x**2 for x in range(1, 6)]
print(squares) # [1, 4, 9, 16, 25]

# Filter a list (only even numbers)
nums = [1, 2, 3, 4, 5, 6]
evens = [x for x in nums if x % 2 == 0]
```
