## Understanding the `__new__` method in Python

- `__new__` method is called when we create an instance of a class.
- We can override this method to customize it's behaviour (often used to implement design patterns like the Singleton pattern).
- After this '__ init__' is called.
- takes in a 'class object', and optionally, *args and **kwargs.
- We will have to return instance from `__new__`, which is taken by `__init__` as self.
- Everything in Python is an object.
- A 'class object' is not instance of that class, but the class itself.
- We can use it to access class attributes (which is represented by static variables in Java).

### Example Usage of `__new__`

```python
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            # calls object's __new__ for applying default behaviour, which is object creation of Singleton class here
            cls._instance = super(Singleton, cls).__new__(cls)   
        return cls._instance

# Usage
instance1 = Singleton()
instance2 = Singleton()

print(instance1 is instance2)  # This will print True, indicating that both variables refer to the same instance.
```

### __ call__ dunder method
- callable(object_name) will return true if the class of object_name implements `__call__` method.
- Implementing `__call__` means we can instantiate it ex. obj = MyClass()
- Since type class implements `__call__`, and all the classes are objects of 'type' class, all the classes are callable.
- Example shown below.
```python
class A:
  def __init__(self, name):
    self.name = name  
  def __call__(self, *args, **kwargs):
    print("{self.name}, call is run")

a = A("Abhishek")
a()    # prints, Abhishek call is run
# We can pass in arguements also
#exampel: a("Abhishek", "Jha")
```
