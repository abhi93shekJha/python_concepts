## Points about importing in Python

1. To make a folder a package add '__ init__.py'.
2. To import between two subfolders, both should be packages. (having '__ init__.py')








## Usage/Examples

```python
my_project
    main_folder
        __init__.py
        sub_folder_1
            __init__.py
            script1.py
            script2.py
        sub_folder_2
            __init__.py
            script3.py
            script4.py
        main_script.py

# Here main_folder has to be a package(using __init__.py) for importing anything from sub_folder_1/script1 to sub_folder_2/script3

# Also, both the subfolders have to be packages (using __init__.py)

# Inside same subfolder use as below,
  from . import script1

# To import sub_folder_1 module inside sub_folder_2 module use
  from ..sub_folder_1 import scrip1/script2
```

