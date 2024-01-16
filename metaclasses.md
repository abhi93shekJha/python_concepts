### Metaclasses basics
- As we know that in python classes themselves are objects, unlike java etc.
- In python, 'type' is a class that creates class object.
- All the classes implicitly implements 'type' class as its metaclass, as shown below.
```python
class MyClass(metaclass=type):
  ...attributes and methods below
```
- When the simple class creation syntax is run (class A:pass), then internally an object of "type" class is created which is a class object.
- Then internally this class object is used to create instance of this class.
- Below example will expain with comments, how class object gets created.
### Note- Metaclass can only create and manipulate class's attributes and methods on the go. Not instance's attributes (what is inside __init__ method) 
```python
class A:
  pass

# When the above syntax is run, an object of 'type' class is created
print(type(A))   # it prints, <class 'type'>

# and we know that type() prints class for any object
# FYI: type(any_function) prints <class 'function'>
# 'type' class creates a class object

# We can create a class using type class as below:
dog_class = type("Dog", (), {"breed":"German Shephard"})
    # type(classname, (Supertype_tuple,), {attributes and methods dict})

# dog_class variable is referencing 'Dog' class (not object).
print(dog_class)     # <class '__main__.Dog'>

class User:
  def __init__(self, name):
    self.name = name
    
  def print_name(self):
    print(self.name)
    
# lets create a class with methods and attributes using "type" class
def give_exam(self):
  print(f"{self.name} Giving Exam!!")
  
Student = type("Student", (User,), {"standard":None, "give_exam":give_exam})

s = Student("John")
s.give_exam()    # John Giving Exam!!
print(s.name)    # John

# So we can inherit from type to manipulate class creation process
# Below code will capitalize the attribute and method names.

class Meta(type):
  # as we know, when an object is created __new__ dunder runs before __init__
  # __new__ can take in params too
  def __new__(cls, class_name, bases_tuple, attr_dict):
    temp_attr = dict()
    for key, value in attr_dict.items():
      temp_attr[key.capitalize()] = value
    print(temp_attr)  
    return type(class_name, bases_tuple, temp_attr)

# when this syntax runs, Meta will manipulate the attributes
class User(metaclass=Meta):
  name = "Abhishek"

  def print_name(self):
    print(f"name is {User.Name}")

user = User()
# print(user.name)  # throws error
# print(user.print_name())   # throws error
print(user.Name)    # prints, Abhishek
user.Print_name()   # prints, name is Abhishek
```
