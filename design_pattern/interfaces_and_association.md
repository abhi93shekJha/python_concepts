### Interface
- These are contracts that we define.
- In python, we do it with the help of abstract classes by subclassing from ABC module.
```python
from abc import ABC, abstractmethod

class MyClass(ABC):

  @abstractmethod
  def my_fun(self):
    pass

class ChildClass(MyClass):

  def my_fun(self):
    print("Overriding abstract method!!")

child_class = ChildClass()
child_class.my_fun()

```
- We write code to interfaces in order to be aligned with SOLID principals.
### Association
- A class having dependency on another object, is called association. (has a relationship)
- There are two types of association, composition and aggregation.
- Composition is an association where when the composite(class containing the object) is destroyed,
component(object within the class) is also destroyed. Example below.
```python
class Engine:

  def start(self):
    print("Engine is starting!!")

class Car:  # Composite

  def __init__(self):
    self.engine = Engine()   # component

  def start_car(self):
    self.engine.start()
    
car = Car()
car.start_car()
```
- Aggregation is an association where when composite is destroyed, component continue to exist. Example below.
```python
class Engine:

  def start(self):
    print("Engine is starting!!")

class Car:

  def __init__(self, engine):
    self.engine = engine

  def start_car(self):
    self.engine.start()

# this reference will continue to exists even if Car is destroyed and can be used in other classes.
engine = Engine()

car = Car(engine)
car.start_car()

```
