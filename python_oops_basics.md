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
## 5. Private and protected in python
- Private members have __(double underscore) before their name.
- Protected members have _(single underscore) before their name.
- Public members have no underscores before their name.
- Note - We can access protected members from anywhere too, it is just recommended not to access them as public members.
- Also, we can access private members too with name mangling, using object_name._ClassName__privatemember.
  
## Inheritance
- isinstance(object, className)
- issubclass(ChildClass, ParentClass)  # True
- All the class implicitly extends from 'object' class.
- Python supports multiple inheritance.
- In case of multiple inheritance, MRO (method resolution order) decides what method or attribute to be called.
- object_name.mro() or object_name.__mro__ shows MRO.

## Polymorphism
Example:
```python
class Animal:
    def __init__(self, type, name):  # type to be mammal or reptile
        self.type = type
        self.name = name

    def _eat(self, food):   # not use it outside of child Class (although can be used)
        print(f"{self.name} is eating, {food}.")

    def make_sound_and_eat(self, food):
        pass

class Cow(Animal):
    def __init__(self, type, name, animal):
        Animal.__init__(self, type, name)  # or
        super().__init__(type, name)    # this way no need to pass self
        self.animal = animal

    def make_sound_and_eat(self, food):
        self._eat(food)
        print("Mooooo!!")

class Dog(Animal):
    def make_sound_and_eat(self, food):
        self._eat(food)
        print("Woof Woof!!")

# can accept any animal
def eat_and_make_sound(animal, food):
    animal.make_sound_and_eat(food)

dog = Dog("Mammal", "Tommy")
cow = Cow("Mammal", "Ganga", "cow")
eat_and_make_sound(dog, "Pedigry")
eat_and_make_sound(cow, "Grass")
```
## Note: Remember that in inheritance, child will have access to all the parent's method including constructor. So, there is no need to add constructor in child unless we want extra attributes initialization inside child.

## super() in python:
- We use super().parent_method() to call a parent's method.
- When using super().__ init__(), no need to pass in self (inside __ init__), it is simply calling the parent's method, just like we call using object.method().
- super() is also called proxy object or "super" object.
- super(MyClass, instance).parent_method() is also one way to call parent's method.
- Here "MyClass" is the class in inheritance hierarchy above which the method search starts, not in the mentioned class.
- And instance is something on which we want to call the method. It is the instance of the Class mentioned as second paramter.
- Although super().parent_method() do the same thing but super(MyClass, instance).parent_name() is needed to resolve any confusion to select method incase of multiple inheritance. Example below.
- Also, method  is called based on method resolution order (MRO). ClassName.__ mro__, prints Class's order to be used for method invocation. Python internally uses some algorithm.
- We generally always use super() (without arguements), otherwise our inheritance hierarchy is complex. super() works in all the cases and runs method using MRO.
### Example below:
```python
# Example 1
class A:
  def __init__(self, a):
      self.a = a

  def my_fun(self):
      print(f"a={self.a} Running inside parent A")

class B(A):
  def __init__(self, a):
      super().__init__(a)    # no need to pass self inside __init__
      A.__init__(self, a)      # this is also one way to call parent __init__, self is needed to be passed
      super(B, self).__init__(a)  # this is another way, telling to start the search of method __init__ from class A

  def my_fun(self):
      super(B, self).my_fun()   # my_fun is being searched in B then A, and it will be run on self object
      print(f"inside B, running my_fun")

b = B(3)
b.my_fun()

# Example 2- showing using super to resolve method confusion in multiple inheritance
class A:
  def my_fun(self):
    print("for parent A, running my_fun")

class B:
  def my_fun(self):
    print("for parent B, running my_fun")

class Child(B, A):
  def my_fun(self):
    super(B, self).my_fun()  # this way of using super will now help us resolving conflict of which class's method to run
# here it will run for A (which is above B in hierarchy)

child = Child()
child.my_fun()   # for parent A, running my_fun
```

