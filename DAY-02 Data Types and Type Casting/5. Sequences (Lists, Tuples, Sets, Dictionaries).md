Built-in Data Collections in Python
===================================

Python has four built-in data types used to store collections of data (often referred to under the umbrella of sequences and collections). Here is a detailed guide for Lists, Tuples, Sets, and Dictionaries.

1. List
-------
Lists are used to store multiple items in a single variable.
- Characteristics:
  * Ordered: The items have a defined order, and that order will not change.
  * Changeable (Mutable): We can change, add, and remove items in a list after it has been created.
  * Allow Duplicates: Since lists are indexed, lists can have items with the same value.
  * Written with square brackets: `[]`

- Example:
  # Creating a list
  fruits = ["apple", "banana", "cherry", "apple"]
  print("List:", fruits)

  # Accessing elements (0-indexed)
  print("First fruit:", fruits[0])

  # Modifying elements
  fruits[1] = "blueberry"
  
  # Adding elements
  fruits.append("orange")
  print("Modified List:", fruits)


2. Tuple
--------
Tuples are used to store multiple items in a single variable.
- Characteristics:
  * Ordered: The items have a defined order, and that order will not change.
  * Unchangeable (Immutable): We cannot change, add, or remove items after the tuple has been created.
  * Allow Duplicates: Like lists, tuples can have duplicate values.
  * Written with round brackets: `()`

- Example:
  # Creating a tuple
  coordinates = (10.0, 20.0, 10.0)
  print("Tuple:", coordinates)

  # Accessing elements
  print("X-Coordinate:", coordinates[0])

  # Attempting to change an item will result in a TypeError:
  # coordinates[0] = 15.0 # This will raise an error


3. Set
------
Sets are used to store multiple items in a single variable.
- Characteristics:
  * Unordered: The items do not have a defined order. You cannot be sure in which order the items will appear.
  * Unchangeable (but you can add/remove items): You cannot change individual items, but you can add new items and remove existing ones.
  * No Duplicates: Every element in a set must be unique. Duplicate values are automatically removed.
  * Unindexed: You cannot access items in a set by referring to an index.
  * Written with curly brackets: `{}`

- Example:
  # Creating a set
  unique_numbers = {1, 2, 3, 3, 4}
  print("Set (duplicates removed):", unique_numbers) # Output: {1, 2, 3, 4}

  # Adding an item
  unique_numbers.add(5)
  
  # Removing an item
  unique_numbers.remove(2)
  print("Modified Set:", unique_numbers)


4. Dictionary
-------------
Dictionaries are used to store data values in key:value pairs.
- Characteristics:
  * Ordered (as of Python 3.7): The items have a defined order.
  * Changeable (Mutable): We can change, add, or remove items after the dictionary has been created.
  * No Duplicates in Keys: Keys must be unique; duplicate keys will overwrite existing values.
  * Written with curly brackets and key:value pairs: `{key: value}`

- Example:
  # Creating a dictionary
  car = {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
  }
  print("Dictionary:", car)

  # Accessing value by key
  print("Car Model:", car["model"])

  # Modifying values
  car["year"] = 2020

  # Adding new key-value pair
  car["color"] = "red"
  print("Modified Dictionary:", car)


Comparison Summary
==================
| Data Type  | Ordered | Changeable (Mutable) | Duplicates Allowed | Syntax |
|------------|---------|----------------------|--------------------|--------|
| List       | Yes     | Yes                  | Yes                | []     |
| Tuple      | Yes     | No                   | Yes                | ()     |
| Set        | No      | No (Items can't be   | No                 | {}     |
|            |         | changed, only added) |                    |        |
| Dictionary | Yes     | Yes                  | No (Keys)          | {k:v}  |
