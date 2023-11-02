## Understanding the `__new__` method in Python

- `__new__` method is called when we create an instance of a class.
- We can override this method to customize it's behaviour (often used to implement design patterns like the Singleton pattern).
- After this '__ init__' is called.
- takes in a 'class object', and optionally, *args and **kwargs.
- Everything in Python is an object.
- A 'class object' is not instance of that class, but the class itself.
- We can use it to invoke class attributes (that is represented by static variables in Java).

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

