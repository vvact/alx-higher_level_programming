    **Everything in python is an Object**


In Python, everything is considered an object. This means that not only data structures like lists, dictionaries, and strings are objects, but also functions, classes, and even integers and other primitive data types are objects. Here's a brief overview of objects in Python:

Everything Is an Object: In Python, objects are instances of classes. Every value, including integers, floats, strings, lists, functions, and custom user-defined objects, is an instance of a class.

Attributes and Methods: Objects have attributes and methods associated with them. Attributes are variables that store data, and methods are functions that can be called on the object. For example, a string object has attributes like length (len) and methods like split() and upper().

Dynamic Typing: Python is dynamically typed, which means you don't need to declare the type of a variable explicitly. The type is determined at runtime based on the object assigned to it. For example, you can assign an integer, then later assign a string to the same variable.

Immutable and Mutable Objects: Objects in Python can be categorized as either immutable or mutable. Immutable objects cannot be changed after they are created (e.g., integers, strings, and tuples), while mutable objects can be modified after creation (e.g., lists, dictionaries, and custom objects).

Custom Objects: You can define your own classes to create custom objects with their own attributes and methods. This is a fundamental concept in object-oriented programming (OOP), and Python is an object-oriented language.

Here's a simple example illustrating some of these concepts:

python
Copy code
# Creating a custom class
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says Woof!")

# Creating instances (objects) of the Dog class
dog1 = Dog("Buddy")
dog2 = Dog("Charlie")

# Accessing object attributes and calling methods
print(dog1.name)  # Accessing attribute
dog2.bark()       # Calling method

# Python objects are dynamic
x = 5
print(type(x))    # Output: <class 'int'>

x = "Hello, World!"
print(type(x))    # Output: <class 'str'>
In this example, dog1 and dog2 are instances of the Dog class, and they have attributes like name and methods like bark(). Additionally, Python's dynamic typing allows you to change the type of a variable (x) as needed.
