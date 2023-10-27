# Python Object-Oriented Programming Concepts

## 1. `help(object_name)`
The `help(object_name)` function is used to display the blueprint of an object. It provides information about the object's class, attributes, and methods.

## 2. Class Object Attribute
Example:

```python
class MyClass:
    # Class object attribute
    x = 5
    
    def __init__(self, name):
        self.name = name
        print(self.x)       # We can access class attribute anywhere across the class,
        print(MyClass.x)    # using `self.` or `ClassName.`, both will give the same value

    def print_name(self):
        print(self.name)

my_class1 = MyClass("Abhishek")   # Prints 5 and 5
my_class2 = MyClass("Sunny")      # Prints 5 and 5

print(my_class1.x)  # Prints 5
print(my_class2.x)  # Prints 5
print(MyClass.x)    # Prints 5

# The class attribute value is the same for all instances of this class.
# We cannot change it using an object.
my_class1.x = 10  # Creates a separate object attribute for my_class1 only.

# We can change it using the class name.
MyClass.x = 10    # This will change it

print(my_class1.x)  # Prints 10
print(my_class2.x)  # Prints 10
print(MyClass.x)    # Prints 10
```

## 3. `@classmethod` and `@staticmethod`
Example:

```python
class MyClass:
    # Class object attribute
    class_object_attr = 20
    
    def __init__(self, x) -> None:
        self.x = x
    
    # Class method having access to the class object
    @classmethod
    def my_class_method(cls, num1, num2):
        print(cls.class_object_attr)
        return cls(num1 + num2)

    # Static method with no access to the class object
    @staticmethod
    def my_static_method(num1, num2):
        return (num1 + num2)

my_class = MyClass(10)

# Both invocations are equivalent
print(MyClass.my_class_method(1, 2))  # Both create a new object
print(my_class.my_class_method(1, 2))

# Both invocations are equivalent
print(MyClass.my_static_method(1, 2))
print(my_class.my_static_method(1, 2))
```
## 4. Attribute Assignment to Class Method
Example:

```python
class MyClass:
    def print_anything():
        print("hey!!")

my_class = MyClass()
my_class.print_anything = "hi!!"

my_class.print_anything()  # Error, `my_class.print_anything` became a string attribute for the `my_class` object
print(my_class.print_anything)  # Prints "hi!!"
```

## Useful commands

python -m venv my_project (create a new virtual environment)

source my_project/bin/activate (start the virtual environment)

pip list (to list installed libraries)

### Django related commands

django-admin --help

django-admin startproject myproject (to start a new project)



### All about constructors in python

```python
'''
 1. Used to instantiate an object, and 
 instance variables are often defined and
 instantiated inside the constructor itself
 '''
 def __init__(self, name):
     self.name = name
     self.next = None

 
 ''' 
 2. We cannot overload a constructor like java. 
 If overloaded, it will take the 
 latest constructor into consideration and 
 not consider the previous implementations.
 
 To achieve constructor overloading, we can
 use @classmethod, which is a python way to do this.
 '''
class Student:
    def __init__(self, name, age, rollno):
        self.name = name
        self.age = age
        self.rollno = rollno

    @classmethod
    def init_with_name_age(cls, name, age):
        return cls(name, age, 0)

    @classmethod
    def create_student_with_rollno(cls, rollno):
        return cls("-", 0, rollno)    

abhishek = Student("Abhishek", 29, 2)
sushant = Student.init_with_name_age("Sushant", 35)
unknown = Student.create_student_with_rollno(29)

print(sushant.rollno)  # 0
print(unknown.name)   # -

# another way is to have keyword arguement or defaut arguement

 # 3. We do not have return type for constructor.
 # 4. No access modifiers for constructors.
 # 5. If no constructor written, an implicit default 
 #    constructor is provide by python
class MyClass:
    pass
my_class = MyClass()
# 6. 
```

