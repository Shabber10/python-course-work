# Day 11: Tuples

Tuples are used to store multiple items in a single variable, similar to lists. However, they are created using parentheses `()`.

## Characteristics of Tuples
- **Ordered**: They maintain the order of insertion.
- **Immutable**: **You CANNOT change, add, or remove items after the tuple has been created.**
- **Allow Duplicates**: Can contain items with the same value.

```python
my_tuple = (1, 2, 3, "apple", True)
```

## Why use Tuples?
- They are faster than lists.
- They make your code safer if the data should not be changed (like configuration settings or days of the week).

## Accessing Tuple Items
Indexing and slicing work exactly like strings and lists.
```python
colors = ("red", "green", "blue")
print(colors[0])  # 'red'
```

## Single Item Tuple
To create a tuple with only one item, you MUST add a comma after the item, otherwise Python will not recognize it as a tuple.
```python
single_tuple = ("apple",)
not_a_tuple = ("apple") # This is just a string
```

## Tuple Packing and Unpacking
```python
# Packing: assigning multiple values to a single tuple
coordinates = (10, 20, 30)

# Unpacking: extracting values back into variables
x, y, z = coordinates
print(x) # 10
print(y) # 20
print(z) # 30
```

Since tuples are immutable, they only have two built-in methods:
- `count()`: Returns the number of times a specified value occurs in a tuple.
- `index()`: Searches the tuple for a specified value and returns the position of where it was found.
