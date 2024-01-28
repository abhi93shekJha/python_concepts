## Writing about Prototype Design Pattern

- We use this design pattern when object creation is a time taking process and we need lots of object without spending time. (eg. Training Dataset object creation, Game object creation)

- We can change only required attributes for the object and can have the same other attributes in the copied instances.

- Idea is to create a shallow copy or deep copy of the existing object. We can use registory design pattern (sometimes called factory here) also to keep the instances in a dictionary and return according to some type.
- __Shallow copy__: Here when we create a clone from an existing prototype object, if the object has objects as it's field/attributes, we assign the same instance to a new reference variables. So if the prototype attribute objects are changed, it will change cloned attributes as well. It is created quickly.
- __Deep copy__: Here we create clone of an object by making deepcopy of its non-primitive attributes as well. It is a resource consuming process, as we iterate on the non-primitive objects recursively to create the copy. Change to one object's non-primitive attribute do not change other object's same attribute as both of them refer to different instances.
### Prototype design pattern without resigstory
1. Creating an interface (using ABC) 'Clonable' with abstract clone method.
2. Implement the interface 'Clonable' in the class for which we need many objects in very less time.  
```python
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing_extensions import override
from enum import Enum
import copy
import time

class Cloneable(ABC):

  @abstractmethod
  def clone(self):
    pass

class Role(Enum):
  ADMIN = 1
  STUDENT = 2
  TEACHER = 3
  
class User(Cloneable):

  def __init__(self, name, age, role):
    self.name = name
    self.age = age
    self.role = role
    time.sleep(5)
  
  @override
  def clone(self):
    return copy.deepcopy(self)

  def __repr__(self):
    return f"{self.name}, {self.age}, {self.role}"


if __name__=="__main__":
  user1 = User(name="Abhishek", age=30, role=Role.ADMIN)
  user2 = user1.clone()

  print(user1)  #prints, Abhishek, 30, Role.ADMIN
  print(user2)  #prints, Abhishek, 30, Role.ADMIN
```
### Prototype design pattern with registory
```python
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing_extensions import override
from enum import Enum
import copy
import time

class Cloneable(ABC):

  @abstractmethod
  def clone(self):
    pass

class Role(Enum):
  ADMIN = 1
  STUDENT = 2
  TEACHER = 3
  
class User(Cloneable):

  def __init__(self, name, age, role):
    self.name = name
    self.age = age
    self.role = role
    time.sleep(5)
  
  @override
  def clone(self):
    return copy.deepcopy(self)

  def __repr__(self):
    return f"{self.name}, {self.age}, {self.role}"

class PrototypeRegistory(ABC):

  @override
  def add_prototype(self, user: User):
    pass

  @override
  def get_prototype(self, role: Role):
    pass

class UserRegistory(PrototypeRegistory):

  def __init__(self) -> None:
    self.registory = dict()
  
  def add_prototype(self, user: User):
    self.registory[user.role] = user

  def get_prototype(self, role: Role):
    if role in self.registory:
      return self.registory[role]

  def clone(self, role):
    return copy.deepcopy(self.registory[role])
    
    

if __name__=="__main__":
  user_registory = UserRegistory()
  
  user_admin = User(name="Abhishek", age=30, role=Role.ADMIN)
  user_registory.add_prototype(user_admin)

  user_student = User(name="Abhishek", age=30, role=Role.STUDENT)
  user_registory.add_prototype(user_student)

  user_teacher = User(name="Abhishek", age=30, role=Role.TEACHER)
  user_registory.add_prototype(user_teacher)
  
  teacher_clone = user_registory.clone(Role.TEACHER)
  student_clone = user_registory.clone(Role.STUDENT)
  admin_clone = user_registory.clone(Role.ADMIN)

  print(teacher_clone)
  print(student_clone)
  print(admin_clone)
  
```

