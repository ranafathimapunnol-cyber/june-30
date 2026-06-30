# ============ VARIABLES & DATA TYPES ============
# Numbers
age = 25
price = 99.99
complex_num = 3 + 4j

# Strings
name = "Kerala"
greeting = 'Hello, World!'
multi_line = """This is a
multi-line string"""

# Booleans
is_beautiful = True
is_rainy = False

# Lists (mutable)
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
fruits[0] = "mango"

# Tuples (immutable)
coordinates = (10, 20)

# Dictionaries (key-value pairs)
person = {
    "name": "John",
    "age": 30,
    "city": "Kochi"
}

# Sets (unique values)
unique_numbers = {1, 2, 3, 3, 4}  # {1, 2, 3, 4}

# None
nothing = None

# ============ TYPE CONVERSION ============
num_str = "123"
num_int = int(num_str)        # 123
num_float = float(num_str)    # 123.0
str_num = str(456)            # "456"
str_bool = str(True)          # "True"

# ============ INPUT & OUTPUT ============
# Print
print("Hello, World!")
print(f"Name: {name}, Age: {age}")  # f-string
print("Name: {}, Age: {}".format(name, age))

# Input
user_input = input("Enter your name: ")
number = int(input("Enter a number: "))

# ============ STRING OPERATIONS ============
text = "DiscoverEase Kerala"
print(text.upper())           # DISCOVEREASE KERALA
print(text.lower())           # discoverease kerala
print(text.title())           # Discoverease Kerala
print(text.split())           # ['DiscoverEase', 'Kerala']
print(text.replace("Kerala", "India"))  # DiscoverEase India
print(text[0:5])              # Disc
print(text[::-1])             # Reverse string
print(len(text))              # Length
print("Kerala" in text)       # True

# ============ LISTS OPERATIONS ============
numbers = [1, 2, 3, 4, 5]
numbers.append(6)             # [1,2,3,4,5,6]
numbers.insert(0, 0)          # [0,1,2,3,4,5,6]
numbers.remove(3)             # [0,1,2,4,5,6]
numbers.pop()                 # Remove last
numbers.pop(0)                # Remove first
numbers.sort()                # Sort ascending
numbers.reverse()             # Reverse order
print(len(numbers))           # Length
print(numbers[1:3])           # Slicing

# List comprehension
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
evens = [x for x in range(10) if x % 2 == 0]  # [0,2,4,6,8]

# ============ DICTIONARY OPERATIONS ============
person = {"name": "John", "age": 30}
person["city"] = "Kochi"       # Add new key
person["age"] = 31             # Update
del person["city"]             # Delete key
print(person.keys())           # dict_keys(['name', 'age'])
print(person.values())         # dict_values(['John', 31])
print(person.items())          # dict_items([('name', 'John'), ('age', 31)])
print(person.get("name"))      # John
print(person.get("country", "India"))  # India (default)

# ============ SET OPERATIONS ============
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1.union(set2))        # {1,2,3,4,5,6}
print(set1.intersection(set2)) # {3,4}
print(set1.difference(set2))   # {1,2}
print(set1.symmetric_difference(set2))  # {1,2,5,6}