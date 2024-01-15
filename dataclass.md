```python
from dataclasses import dataclass

@dataclass
class MyClass:
  # these are not class attributes,
  # but are object attributes, and will be different
  # for different objects
  x: str
  y: int

# we should give keyword arguments to the constructor, 
# to avoid any confusion
my_class = MyClass(x=2, y=3) # note here I am providing both variables as integer
print(my_class)  # prints, MyClass(x=2, y=3)
```
- dataclass annotation removes some boilerplate code.
- It provide under the hood implementation of __repr __, __init __ and __eq __ dunder methods.
- So, it provides special power to our objects, as print(object_name) will always print in the format shown in example.
- obj1 == obj2, will print True, if contents are same, otherwise false, unlike default implementation which will give False,
since both the variables will refer to different objects.
- We can see that __init __ is hidden in the above implementation.
