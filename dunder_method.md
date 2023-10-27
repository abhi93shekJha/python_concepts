# Dunder methods (aka special methods or magic methods)
- methods starts and ends with __ (two underscors), eg. __ str__, __ len__
- It is invoked for an object by the interpreter in response to some specific operation or built in function.
- def __ init__ is called when object is instantiated (some operation).
- def __ len__ is called when len([1,2,3]) is used (built in function). This is called in the list class.
- We can customize the behaviour of objects using these methods.
- object class has default implementation of all the dunder methods available.
### For example
```python
  class SuperList(list):
    # overriding what len() does
    def __len__(self):
      return 5

  super_list = SuperList()
  super_list.append(1)
  super_list.append(2)
  print(super_list[0])  # prints 1
  print(len(super_list))   # always prints 5
  super_list.append(3)
  print(len(super_list))   # always prints 5
```
### Few more usage of dunder methods.
```python
  class MyClass():
    # few dunder methods are
    def __str__(self):
      print("hi!!")
    def __len__(self):
      return 5
    def __del__(self):
      return 'deleted'
    def __call__(self):
      return "called"
    def __getitem__(self, i):
      return i;

  my_class = MyClass()
  print(my_class.__str__())
  print(str(my_class))   # runs __str__
  print(my_class())  # runs __call__
  print(my_class[1])    # runs __getitem__, you can imagine now that this is used in list, tuple etc classes.
```
