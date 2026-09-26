================================================================================
WHAT I LEARNED FROM THIS PROJECT

This document contains the main Python concepts, techniques, and object-oriented
programming principles that I learned and practiced while building this project.

================================================================================

PYTHON MODULES AND name
================================================================================

Every Python file is a module, and every module has a special name variable.

When a Python file is executed directly, its name value becomes:

"__main__"


When the file is imported into another Python file, its name becomes the
name of the module.

Example:

# ahmet.py
print(__name__)


If ahmet.py is executed directly:

__name__ == "__main__"


If ahmet.py is imported:

import ahmet

print(ahmet.__name__)


The output will be:

ahmet


This is why Python programs commonly use:

if __name__ == "__main__":
    main()


This ensures that the main part of the program runs only when the file is
executed directly and not when it is imported as a module.

================================================================================
2. SHEBANG

A shebang is a special line written at the beginning of a script.

For Python:

#!/usr/bin/env python3


It tells the operating system to find the Python 3 interpreter and use it to
execute the file.

For example:

./program.py


To execute a Python file directly, it needs executable permission:

chmod +x program.py


Then it can be executed with:

./program.py


Alternatively, the file can be executed using:

python3 program.py


In this case, executable permission is not required.

Important:

The shebang does NOT make a file executable by itself.
The file must also have execute permission.

================================================================================
3. CLASSES AND INSTANCES

A class is a blueprint used to create objects.

Example:

class Plant:
    pass


An object created from a class is called an instance.

Example:

plant1 = Plant()


Here:

Plant   -> Class
plant1  -> Instance


A class can have multiple instances:

plant1 = Plant()
plant2 = Plant()


Each instance can have its own attributes and values.

For example:

plant1 = Plant("Cactus", 25, 30)


Here, plant1 is an instance of the Plant class.

================================================================================
4. CONSTRUCTOR - init()

The init() method is called automatically when a new object is created.

Example:

class Plant:

    def __init__(self, name, age):
        self.name = name
        self.age = age


Creating an object:

plant = Plant("Cactus", 5)


The values are passed to the init() method when the object is created.

================================================================================
5. self

The self keyword refers to the current instance of a class.

Example:

class Plant:

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


Here, self.name belongs to the current object.

For example:

plant1 = Plant("Cactus")

print(plant1.get_name())


self allows each object to store and access its own data.

================================================================================
6. range()

The range() function is used to generate a sequence of numbers.

Example:

for i in range(5):
    print(i)


Output:

0
1
2
3
4


range() can also accept start, stop, and step values:

range(start, stop, step)


Example:

for i in range(2, 10, 2):
    print(i)


Output:

2
4
6
8


The stop value is not included.

================================================================================
7. round()

The round() function is used to round numbers.

Example:

number = 3.14159

print(round(number, 2))


Output:

3.14


The second argument specifies how many decimal places should be kept.

================================================================================
8. PROTECTED ATTRIBUTES

A single underscore (_) is commonly used to indicate that an attribute or
method is intended for internal or protected use.

Example:

class Plant:

    def __init__(self):
        self._name = "Cactus"


The attribute can technically still be accessed:

plant._name


However, the underscore is a convention that tells other developers that
the attribute is intended for internal use.

A single underscore does NOT prevent access.

================================================================================
9. NAME MANGLING

Python uses name mangling for attributes and methods that start with
two underscores (__).

Example:

class Plant:

    def __init__(self, name):
        self.__name = name


Python internally changes the name to something similar to:

self._Plant__name


Therefore, this will not normally work:

plant.__name


However, it can technically be accessed using:

plant._Plant__name


Name mangling is mainly used to prevent accidental name conflicts and to
discourage direct access to internal attributes.

It is important to remember that Python does not have truly private attributes
in the same way as some other programming languages.

================================================================================
10. INSTANCE METHODS

An instance method is a method that works with a specific object.

It normally receives self as its first parameter.

Example:

class Plant:

    def get_name(self):
        return self.name


The method is called through an instance:

plant.get_name()


Instance methods can access and modify instance attributes.

================================================================================
11. @staticmethod

A static method belongs to a class but does not need access to the instance
or the class itself.

Example:

class Plant:

    @staticmethod
    def is_valid_temperature(temperature):
        return 0 <= temperature <= 50


It can be called directly through the class:

Plant.is_valid_temperature(25)


A static method does not automatically receive self or cls.

================================================================================
12. @classmethod

A class method works with the class itself instead of a specific instance.

The first parameter is conventionally called cls.

Example:

class Plant:

    count = 0

    @classmethod
    def get_count(cls):
        return cls.count


It can be called using:

Plant.get_count()


Class methods are useful when working with class-level data or when creating
alternative constructors.

================================================================================
13. self AND cls

self:

self refers to the current instance.


Example:

def get_name(self):
    return self.name


cls:

cls refers to the class itself.


Example:

@classmethod
def create_default(cls):
    return cls("Unknown")


In short:

self -> Current object
cls  -> Current class

================================================================================
14. METHOD TYPES

There are three main types of methods commonly used in Python classes.

Instance Method
    First parameter: self
    Works with an instance.

Class Method
    First parameter: cls
    Works with the class.

Static Method
    No automatic self or cls parameter.
    Provides functionality related to the class without needing
    instance or class data.


Summary:

Instance Method  -> self
Class Method     -> cls
Static Method    -> no automatic parameter

================================================================================
15. NESTED CLASSES

A class can be defined inside another class.

This is called a nested class.

Example:

class Plant:

    class Leaf:

        def __init__(self, color):
            self.color = color

    def __init__(self, name):
        self.name = name


The nested class can be accessed using:

leaf = Plant.Leaf("Green")

print(leaf.color)


Nested classes can be useful when a class is closely related to another class
and is mainly used within that context.

================================================================================
16. INHERITANCE

Inheritance allows one class to inherit attributes and methods from another
class.

Example:

class Plant:

    def grow(self):
        print("Plant is growing")


class Cactus(Plant):
    pass


Cactus inherits from Plant.

Therefore:

cactus = Cactus()
cactus.grow()


Output:

Plant is growing


Terminology:

Plant  -> Parent / Base / Superclass
Cactus -> Child / Derived / Subclass


Inheritance helps reduce code duplication and allows common functionality
to be defined once in a parent class.

================================================================================
17. METHOD OVERRIDING

A child class can redefine a method inherited from its parent class.

This is called method overriding.

Example:

class Plant:

    def grow(self):
        print("Plant is growing")


class Cactus(Plant):

    def grow(self):
        print("Cactus is growing differently")


Now:

cactus = Cactus()
cactus.grow()


Output:

Cactus is growing differently


The Cactus class has overridden the grow() method from Plant.

================================================================================
18. super()

The super() function is used to access methods from a parent class.

It is especially useful when calling the parent's init() method.

Example:

class Plant:

    def __init__(self, name):
        self.name = name


class Cactus(Plant):

    def __init__(self, name, spines):
        super().__init__(name)
        self.spines = spines


Here:

super().__init__(name)


calls the init() method of the parent class.

This allows us to reuse the parent's initialization code instead of
writing it again.

Example:

cactus = Cactus("Cactus", 100)

print(cactus.name)
print(cactus.spines)


Here:

name   -> Initialized by Plant
spines -> Initialized by Cactus

================================================================================
19. super() WITH OTHER METHODS

super() can also be used to call other methods from the parent class.

Example:

class Plant:

    def grow(self):
        print("Plant is growing")


class Cactus(Plant):

    def grow(self):
        super().grow()
        print("Cactus grows with very little water")


Calling:

cactus = Cactus()
cactus.grow()


Output:

Plant is growing
Cactus grows with very little water


This allows the child class to keep the parent's behavior and add
additional behavior.

================================================================================
20. INHERITANCE + super()

A complete example:

class Plant:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def grow(self):
        print(f"{self.name} is growing.")


class Cactus(Plant):

    def __init__(self, name, age, spines):
        super().__init__(name, age)
        self.spines = spines

    def grow(self):
        super().grow()
        print("Cactus grows with very little water.")


Usage:

plant1 = Cactus("Cactus", 5, 100)

print(plant1.name)
print(plant1.age)
print(plant1.spines)

plant1.grow()


In this example:

- Cactus inherits from Plant.
- Cactus uses super().__init__() to call the parent constructor.
- Cactus adds its own spines attribute.
- Cactus overrides the grow() method.
- super().grow() calls the parent's grow() method.
- Cactus then adds its own behavior.

================================================================================
21. OBJECT-ORIENTED PROGRAMMING CONCEPTS I LEARNED

While working on this project, I learned and practiced:

- Classes
- Instances
- Constructors (__init__)
- Instance methods
- Class methods
- Static methods
- self
- cls
- Nested classes
- Inheritance
- Parent / Base classes
- Child / Derived classes
- Method overriding
- super()
- Encapsulation
- Name mangling
- Protected attributes
- Modules
- Imports
- __name__
- if __name__ == "__main__"
- Shebang
- Linux file permissions
- range()
- round()

================================================================================
22. FINAL NOTES

Building this project helped me understand how Python works beyond basic
syntax.

I learned how classes and objects can be structured, how inheritance allows
code reuse, how super() connects child and parent classes, and how Python
handles modules and script execution.

The project also helped me understand the difference between instance
methods, class methods, and static methods, as well as concepts such as
encapsulation, name mangling, and protected attributes.

Overall, this project gave me practical experience with Python's
Object-Oriented Programming principles and helped me write more structured,
reusable, and maintainable code.

================================================================================
END OF README
