# Data Structure

## Is a way to organize and store data in a computer so that it can be accessed and modified efficiently.

## Types of Data Structures
1. list[] - A collection of items that can be of different types. It is ordered and mutable.
2. tuple() - A collection of items that can be of different types. It is ordered and immutable.
3. set{} - A collection of unique items that can be of different types. It is unordered and mutable.
4. dict{} - A collection of key-value pairs. It is unordered and mutable.

## How to choose a data structure?
- Standard Library - Use the built-in data structures provided by the programming language.
  - Built-in Modules - Use data structures from built-in modules like `collections` in Python.
      1. Functions - e.g., print(), len(), etc. can be used to manipulate data structures.
      2. <Class 'list'> - A built-in data structure that can be used to store a collection of items.
      3. <Class 'tuple'> - A built-in data structure that can be used
      4. <Class 'set'> - A built-in data structure that can be used to store a collection of unique items.
      5. <Class 'dict'> - A built-in data structure that can be used to store a collection of key-value pairs.
- Function vs Method
    - Function - A block of code that performs a specific task and can be called by its name. It is not associated with any object.
        ```python
        costs = [10, 20, 15]
        len(costs)
        ```
    - Method - A function that is associated with an object and can be called on that object. It is defined within a class and can access the attributes of the class.
        ```python
        costs = [10, 20, 15]
        costs.remove(10)
        ```