# Python Coding Assessment Solutions

import math

# add numbers
def add_numbers(num1, num2):
    """
    
    """
    return num1 + num2

# is even
def is_even(number):
    """
   
    """
    return number % 2 == 0

# reverse string
def reverse_string(text):
    """
   
    """
    return text[::-1]

# count vowels
def count_vowels(text):
    """
    
    """
    vowels = 'aeiou'
    count = sum(1 for char in text.lower() if char in vowels)
    return count

# calculate factorial
def calculate_factorial(n):
    """
    
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        return 1
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

# apply_decorator
def decorator_func(func):
    """
    
    """
    def wrapper(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return wrapper

def apply_decorator(func):
    """
    
    """
    return decorator_func(func)

# Sort List of Tuples
def sort_by_age(list_of_tuples):
    """
    S
    """
    return sorted(list_of_tuples, key=lambda x: x[1])

# Merge Dictionaries
def merge_dicts(dict1, dict2):
    """
   
    """
    merged = dict1.copy() 
    for key, value in dict2.items():
        if key in merged:
            merged[key] += value
        else:
            merged[key] = value
    return merged

# Class Creation
class Car:
    def __init__(self, make, model, year):
        """
        
        """
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        """
        
        """
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")

# Functions and class
if __name__ == "__main__":
    # Test add numbers
    print("add_numbers(5, 3):", add_numbers(5, 3)) 

    # Test is_even
    print("is_even(4):", is_even(4))  

    # Test reverse string
    print("reverse_string('Nickson'):", reverse_string("Nickson"))  

    # Test count vowels
    print("count_vowels('Lalat Niqson'):", count_vowels("Lalat Niqson")) 

    # Test calculate factorial
    print("calculate_factorial(5):", calculate_factorial(3)) 

    # Test apply decorator
    @apply_decorator
    def sample_function():
        print("Function Called")

    sample_function()
    
    # Test sort_by_age
    print("sort_by_age([('Alice', 30), ('Bob', 25), ('Charlie', 35)]):",
          sort_by_age([("Alice", 30), ("Bob", 25), ("Charlie", 35)]))
    
    # Test merge_dicts
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'b': 3, 'c': 4}
    print("merge_dicts(dict1, dict2):", merge_dicts(dict1, dict2))
    

    # Test Car class
    car = Car("Toyota", "Corolla", 2020)
    car.display_info()  
