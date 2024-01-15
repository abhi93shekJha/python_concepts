- In Java we know that supertype reference can refer to a subtype instance,
- Similarly, in python a reference can be assigned any instance and any method can be called.
- If the object has the method, it will run, otherwise throws Attribute Error.
- Helps in implementing polymorphism, code reusability, simplified interface etc.
- All the benifits of polymorphism in java will be applied here.
- Example below:
```python
class Parent_A:
  def my_fun(self):
    print("This is parent A")

class Child_B(Parent_A):
  def my_fun(self):
    print("This is child B")

class Child_C(Parent_A):
  def my_fun(self):
    print("This is child C")

def run_my_fun(obj):
  obj.my_fun()

if __name__ == "__main__":
  parent_A = Parent_A()
  child_B = Child_B()
  child_C = Child_C()
  for obj in [parent_A, child_B, child_C]:
    run_my_fun(obj)
    
```
