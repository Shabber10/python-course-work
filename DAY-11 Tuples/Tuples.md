# DAY-11 Tuples

Tuples are used to store multiple items in a single variable. 
A tuple is a collection which is ordered and **unchangeable** (immutable).

## 1. Tuple Characteristics and Definition
- **Ordered:** The items have a defined order, and that order will not change.
- **Unchangeable (Immutable):** We cannot change, add or remove items after the tuple has been created.
- **Allow Duplicates:** Since tuples are indexed, they can have items with the same value.

**Input:**
```python
mytuple = ("apple", "banana", "cherry", "apple")
print(mytuple)
print(len(mytuple))
print(type(mytuple))
```
**Output:**
```text
('apple', 'banana', 'cherry', 'apple')
4
<class 'tuple'>
```

## 2. Creating Tuples with One Item
To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
**Input:**
```python
thistuple = ("apple",)
print(type(thistuple))

not_a_tuple = ("apple")
print(type(not_a_tuple))
```
**Output:**
```text
<class 'tuple'>
<class 'str'>
```

## 3. Accessing Tuple Items
You can access tuple items by referring to the index number, inside square brackets.
**Input:**
```python
thistuple = ("apple", "banana", "cherry", "orange")
print(thistuple[1])
print(thistuple[-1])
print(thistuple[1:3])
```
**Output:**
```text
banana
orange
('banana', 'cherry')
```

## 4. Updating Tuples (The Workaround)
Since tuples are immutable, you cannot change them directly. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
**Input:**
```python
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)
```
**Output:**
```text
('apple', 'kiwi', 'cherry')
```

## 5. Unpacking a Tuple
When we create a tuple, we normally assign values to it. This is called "packing" a tuple. We are also allowed to extract the values back into variables. This is called "unpacking".
**Input:**
```python
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)

# Using Asterisk* (if number of variables is less than items)
fruits2 = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits2
print(red)
```
**Output:**
```text
apple
banana
['cherry', 'strawberry', 'raspberry']
```

## 6. Joining and Multiplying Tuples
**Input:**
```python
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)
```
**Output:**
```text
('a', 'b', 'c', 1, 2, 3)
('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')
```

## 7. Tuple Methods
Tuples have only two built-in methods.
**Input:**
```python
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
print(thistuple.count(5)) # Returns number of times 5 occurs
print(thistuple.index(8)) # Returns first index of 8
```
**Output:**
```text
2
3
```
