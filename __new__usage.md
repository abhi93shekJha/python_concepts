## Understanding the `__new__` Method in Python

`__new__` method is called when we create an instance of a class. we can override this method to customize it's behaviour (often used to implement design patterns like the Singleton pattern).

Takes in the class(cls) as variable in parameter, access the class variables ('_instance' in this case, which remains same for every new object created)

### Example Usage of `__new__`

```python
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

# Usage
instance1 = Singleton()
instance2 = Singleton()

print(instance1 is instance2)  # This will print True, indicating that both variables refer to the same instance.

