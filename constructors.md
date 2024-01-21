
## All about constructors in python

```python
'''
Used to instantiate an object,
instance variables are often defined and
instantiated inside the constructor itself
 '''
 def __init__(self, name):
     self.name = name
     self.next = None
```
- We cannot overload a constructor like java.
- If overloaded, it will take the latest constructor into consideration and not consider the previous implementations.
 
 To achieve constructor overloading, we can use @classmethod, which is a python way to do this.
 ```python
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
```
Another way is to have keyword arguement or defaut arguement

3. We do not have return type for constructor.
4. No access modifiers for constructors.
5. If no constructor written, an implicit default constructor is provide by python
```python
class MyClass:
    pass
my_class = MyClass()
```
6. Note that like java, it is not mandatory to call parent's constructor if a construtor is present in parent.
Example below.
```python
class A_Parent:
  def __init__(self, a, b):
    self.a = a
    self.b = b

class B_Child(A_Parent):
  def __init__(self, c, d):
    # not necessary to call super().__init__(4, 5)
    self.c = c
    self.d = d

child = B_Child(1, 3)
print(child.a) # this will throw an error, as it will assume child class don't have a and b, since no call to super constructor
```
