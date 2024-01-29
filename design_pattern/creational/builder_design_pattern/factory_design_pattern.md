### Factory Design Pattern
- Client can create objects without knowing about the Class for which he/she is creating the object.
- Helpful when we provide third party library to client, so the clients will be able to create object using some factory class and if in future we decide to change the class name(of which object is created), or we decided to modify some logic of object creation in newer version of the library, client's code will have backward compatibility.
- So basically in a case we don't want to expose the class's name and object creation logic, OR we want to provide a clean interface for creating different family of objects with very little code, we can use this design pattern.
- Below examples will clarify the concept more.
### Simple Factory
- We use class/static method for simple factory, and if-else condition for returning objects.
```python
from enum import Enum
from abc import ABC
from typing import Optional

class Role(Enum):
  STUDENT = 1
  TEACHER = 2
  ADMIN = 3
  
class User():
  def __init__(self, name, role) -> None:
    self.name = name
    self.role = role

  def __repr__(self):
    return f"{self.name}, {self.role}"

class Student(User):
  pass

class Teacher(User):
  pass

class Admin(User):
  pass

class UserFactory:
  @classmethod
  def create_user(cls, name, role):
    if role == Role.STUDENT:
      return Student(name, role)
    elif role == Role.TEACHER:
      return Teacher(name, role)
    elif role == Role.ADMIN:
      return Admin(name, role)

if __name__=="__main__":
  user_student: Optional[User] = UserFactory.create_user("Abhishek", Role.STUDENT)
  user_teacher: Optional[User] = UserFactory.create_user("Ramesh", Role.TEACHER)
  user_admin: Optional[User] = UserFactory.create_user("Suresh", Role.ADMIN)

  print(user_student)
  print(user_teacher)
  print(user_admin)
```
### Factory method
- In Simple factory, if we want to provide a new object, we will have add conditions in the factory class, which is not a good design practice as it violates OCP.
- So, it is difficult extent factory.
- Factory method solves this.
- Here, we have different factories for creating different objects.
```python
from enum import Enum
from abc import ABC, abstractmethod
  
class Role(Enum):
  STUDENT = 1
  TEACHER = 2
  ADMIN = 3
  
class User():
  def __init__(self, name, role) -> None:
    self.name = name
    self.role = role

  def __repr__(self):
    return f"{self.name}, {self.role}"

class Student(User):
  pass

class Teacher(User):
  pass

class Admin(User):
  pass

class UserFactory(ABC):
  @abstractmethod
  def create_user(self, name, role):
    pass

class StudentFactory(UserFactory):
  def create_user(self, name, role):
    return Student(name, role)
    
class TeacherFactory(UserFactory):
  def create_user(self, name, role):
    return Teacher(name, role)
    
if __name__=="__main__":
  student_factory = StudentFactory()
  student: User = student_factory.create_user("Abhishek", Role.STUDENT)

  teacher_factory = TeacherFactory()
  teacher: User = teacher_factory.create_user("Jha", Role.TEACHER)

  print(student)
  print(teacher)
```
### Abstract Factory
- This is an extention of Factory method, which helps create a family of objects.
- Here we have factory for a group of objects which belong to same family.
- Example explains better, given below.
```python
from abc import ABC, abstractmethod
  
class Button(ABC):
  @abstractmethod
  def render(self):
    pass

class DarkButton(Button):
  def render(self):
    return "Rendering Dark Button!!"

class LightButton(Button):
  def render(self):
    return "Rendering Light Button!!"

class Checkbox(ABC):
  @abstractmethod
  def render(self):
    pass

class DarkCheckBox(Checkbox):
  def render(self):
    return "Rendering Dark Checkbox!!"

class LightCheckBox(Checkbox):
  def render(self):
    return "Rendering Light Checkbox!!"

class UIFactory(ABC):
  @abstractmethod
  def create_button(self):
    pass

  @abstractmethod
  def create_checkbox(self):
    pass

class DarkUIFactory(UIFactory):
  def create_button(self):
    return DarkButton()

  def create_checkbox(self):
    return DarkCheckBox()

class LightUIFactory(UIFactory):
  def create_button(self):
    return LightButton()

  def create_checkbox(self):
    return LightCheckBox()
  
def create_ui(factory):
  button = factory.create_button()
  checkbox = factory.create_checkbox()
  print(button.render())
  print(checkbox.render())

light_factory = LightUIFactory()
create_ui(light_factory)

dark_factory = DarkUIFactory()
create_ui(dark_factory)

```
