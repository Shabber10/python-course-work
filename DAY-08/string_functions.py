# ==========================================
# PYTHON BUILT-IN STRING FUNCTIONS EXAMPLES
# ==========================================

print("--- 1. CASE MANIPULATION ---")
text = "hello WORLD from Python"
print(f"Original       : '{text}'")
print(f"upper()        : '{text.upper()}'")        # Converts to uppercase
print(f"lower()        : '{text.lower()}'")        # Converts to lowercase
print(f"capitalize()   : '{text.capitalize()}'")   # Capitalizes first letter only
print(f"title()        : '{text.title()}'")        # Capitalizes first letter of each word
print(f"swapcase()     : '{text.swapcase()}'\n")   # Swaps uppercase to lowercase and vice versa


print("--- 2. TRIMMING / STRIPPING WHITESPACE ---")
messy_text = "   too much space   "
print(f"Original       : '{messy_text}'")
print(f"strip()        : '{messy_text.strip()}'")  # Removes leading and trailing whitespace
print(f"lstrip()       : '{messy_text.lstrip()}'") # Removes leading (left) whitespace
print(f"rstrip()       : '{messy_text.rstrip()}'\n")# Removes trailing (right) whitespace


print("--- 3. SPLITTING AND JOINING ---")
csv_data = "apple,banana,cherry,orange"
print(f"Original string: '{csv_data}'")

# split() - Splits string into a list based on a separator
fruits_list = csv_data.split(",")
print(f"split(',')     : {fruits_list}")

# join() - Joins a list of strings into a single string with a separator
joined_text = " | ".join(fruits_list)
print(f"join(' | ')    : '{joined_text}'\n")


print("--- 4. SEARCHING AND COUNTING ---")
sentence = "The quick brown fox jumps over the lazy dog."
print(f"Original       : '{sentence}'")

# count() - Counts occurrences of a substring
print(f"count('o')     : {sentence.count('o')} times")

# find() - Returns the lowest index of the substring (-1 if not found)
print(f"find('fox')    : index {sentence.find('fox')}")

# index() - Like find, but raises an error if not found
print(f"index('fox')   : index {sentence.index('fox')}")

# startswith() and endswith() - Returns True/False
print(f"startswith('The'): {sentence.startswith('The')}")
print(f"endswith('.')    : {sentence.endswith('.')}\n")


print("--- 5. REPLACING TEXT ---")
greeting = "Hello, World!"
print(f"Original       : '{greeting}'")

# replace() - Replaces occurrences of a substring with another
new_greeting = greeting.replace("World", "Python")
print(f"replace()      : '{new_greeting}'\n")


print("--- 6. CHECKING STRING CONTENT ---")
alpha_str = "Python"
digit_str = "12345"
alnum_str = "Python123"

print(f"'{alpha_str}'.isalpha()  : {alpha_str.isalpha()}") # True if all characters are letters
print(f"'{digit_str}'.isdigit()  : {digit_str.isdigit()}") # True if all characters are numbers
print(f"'{alnum_str}'.isalnum()  : {alnum_str.isalnum()}") # True if alphanumeric (letters + numbers)
print(f"'{alpha_str}'.islower()  : {alpha_str.islower()}") # True if all characters are lowercase
