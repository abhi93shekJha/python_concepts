# Python modules and importing 
- A python script (file_name.py) is a module.
- We use snake case for naming python modules (ex. module_name.py).
- When we have multiple modules in a folder, we add an empty "__ init__.py" file in the folder to make it a package.
- A module when imported is compiled by cpython and the compiled file is kept inside __pycache__ folder for quick access.
- 
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
