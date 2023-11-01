# Python modules and importing 
- A python script (file_name.py) is a module.
- We use snake case for naming python modules (ex. module_name.py).
- When we have multiple modules in a folder, we add an empty "__ init__.py" file in the folder to make it a package.
- A module when imported is compiled by cpython and the compiled file is kept inside __pycache__ folder for quick access.
## Important points about if __ name__=='__ main__':
- __ name__ shows the name of the module, which is generally script name.
- only the script under execution, __ name__ shows as "__ main__".
- we use if __ name__=="__ main__", because, if not used, when this module is imported, it's functions can be automatically called, when the importing script is run.
- if all the function calls is placed inside the check if __ name__=='__ main__', when this script is imported these functions won't be called from importing script.
[## Example here](python_modules)

## Important points for importing
- When importing, we should not use *.
- Otherwise importing module methods may behave differently. Example shown below.
- We should use module_name.method_name for using methods of imported module. This will make distinction between same method names.
```python
# some_utility.py
def max(temp_list):
  return temp_list[-1]   # always returns last element of list

# main.py
from some_utility import *
print(max([4, 1, 3, 2]))   # this will print 2
# the above method should print 4, using built-in max method.

# above code can be written as below
import some_utility as su
print(max([4, 1, 3, 2]))   # this will print 4
print(su.max([4, 1, 3, 2]))   # this will print 2
```
## Few python built-in modules
```python
import sys
first_arg = sys.argv[1]
sec_arg = sys.argv[2]

print(first_arg)  # first
print(sec_arg)   # 23
# python3 main.py "first" 23
```
### pypi org for third party packages
- pip3 list  (to get list of install packages)
### Few important built-in modules
```python
from collections import Counter, defaultdict, OrderedDict

l = [1, 2, 3, 4 ,4, 4, 6, 1, 2, 3]
print(Counter(l)) # Counter({4: 3, 1: 2, 2: 2, 3: 2, 6: 1})

str = "daf dfas khadsf khfads"
print(Counter(str)) # Counter({'d': 4, 'a': 4, 'f': 4, ' ': 3, 's': 3, 'k': 2, 'h': 2})

d = {'a':1}
d['b'] = 2
d['c'] = 3

d2 = {'a':1}
d2['c'] = 3
d2['b'] = 2

print(d==d2)  # True  
# == checks for value not object, and since dictionary is unordered, so it will print out "True"
print(d is d2) # False
# 'is' checks for object, and both d and d2 are referring to different objects, so prints out "False"

d1 = OrderedDict()
d1['a'] = 1
d1['b'] = 2

d2 = OrderedDict()
d2['b'] = 2
d2['a'] = 1

print(d1==d2)  # False, both are different values
# unlike dictionary, OrderedDict maintains the order, slower that dictionary

# defaultdict
# first object should be a callable, which is a funtion
d = defaultdict(int, {'a':1, 'b':2})  # used int as int() outputs 0
print(d[1])    # prints 0

d = defaultdict(lambda: 5, {'a':1, 'b':2})
print(d[2])     # prints 5
```
