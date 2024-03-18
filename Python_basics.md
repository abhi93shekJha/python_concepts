- A programming language is a set of instructions we give to a machine for it to execute.

- **Compilers and Interpreters:**

    - We write source code, and either an interpreter or a compiler converts them into machine-level language (0 and 1).

    - An interpreter reads line by line and converts it.

    - A compiler takes the entire source code in at one time and converts it into a binary file(0s and 1s) to be read by the machine.
      (Actually the source code is first converted to bytecode (.class files) and then JVM takes in the bytecode and converts it to machine readable instructions. The JVM uses Just In Time and other optimisation techniques to improve the performance of the conversion.)

    - Both interpreter and compiler are codes written by humans. They act as a translator to convert human-readable codes to machine-readable code.

- **Fact:**

    - Python programs are first compiled (into bytecodes(.pyc files)) by interpreter and then interpreted by the interpreter.
    - Bytecode is platform independent intermediate code, which is interpreted later in case of python.
    - Platform independent means, it can run on different os, it only requires specific Virtual machine (JVM or PVM) to execute irrespective of software or hardware specifications.

- **About interpreters:**

    - The Python code is run by an interpreter (e.g., CPython, Jython, PyPy, etc., interpreters written in C, Java, or Python languages, respectively).

    - It is first converted into bytecode(.pyc files) by interpreting line by line, which in turn is fed to the CPython virtual machine (CPython VM) which iterprets it line by line to convert it to machine readable instructions. After this, it runs on our machine (laptop, mobile, etc.).

    - When we download Python, we actually download the CPython interpreter, and all the documentations are written according to the CPython interpreter.

- **Expression and statement:**

    - `iq = 100`

    - `user_age = iq / 5`
 
    - If it is a complete line of code, it is an statement. If it produces a value, it is an expression.

    - Here, `iq / 5` is called an expression (since it is calculating something), and the complete line `user_age = iq / 5` is an statement (where we are calculating age and assigning it to the `user_age` variable).
    

- **Augmented assignment operator:**

    - Example: `a += 2` or `a /= 2`

- **Type conversion:**

    - Example: `int('100')`, `str(100)`

- **List unpacking:**

    - `a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]`

    - `print(a)   # 1`

    - `print(b)   # 2`

    - `print(c)   # 3`

    - `print(other)   # [4, 5, 6, 7, 8], prints a list`

    - `print(d)   # 9`

- **Dictionaries:**

    - Dictionaries are unordered.

    - From Python 3.7, dictionaries are ordered in the order they are added.

    - Key can only be immutable objects. Eg. "jha", 12, True, (1, 2, 3).

    - We can create a dictionary using `dict(key=value)`. Ex. `my_dict = dict(a=24, b=25)`. this will create {"a":24, "b":25}. Please mind that in "dict(a=24, b=25)" a and b are not strings, these are keyword arguments.

    - `dict.popitem()`, used to remove the last item (key, value pair) from the dictionary. Used for destructively iterating over a dictionary.

    - `my_dict.items()` = [(key1, val1), (key2, val2), (key3, val3)].
- **Tuples:**

    - Tuples are immutable. They cannot be modified.
    - Adding, deleting or assigning element to a tuple will throw error.

    - Similar to a list, `a, b, c, *other = (1, 2, 3, 4, 5, 6, 7)`

    - `print(a)      # 1`

    - `print(other)  # [4, 5, 6, 7], prints a list`

- **Sets:**

    - Sets are unordered unique sets of items.

    - You cannot access them using an index.

    - O(1) time check for item existence.

    - They support all mathematical set operations, e.g., Union, isDisjoint, isSubset, isSuperSet, difference, differenceUpdate, intersection, etc.

- **Logical Operators:**

    - `and` and `or` are short-circuit in Python.

- **`is` vs `==`:**

    - `==` checks for values.

    - `is` checks for the same object in memory.

    - Example:

        - `[1, 2, 3] == [1, 2, 3]`  # True

        - `[1, 2, 3] is [1, 2, 3]`  # False (because both list objects are created in different memory locations)

        - `1 is 1`                  # True

        - `'abc' is 'abc'`          # True (both are in the same location, so it's true)

- **for and while:**

    - The `else` block with `for` and `while` loops will not execute if there is a `break` encountered.

- **Functions:**

    1. **Default parameters:**

        ```python
        def myfun(name='Abhishek', age=29):
            print(f'Name is {name}, age is {age}')
        ```

        - `myfun('Sunny')`   # prints "Name is Sunny, age is 29"

    2. **Keyword arguments:**

        ```python
        def myfun(name, age):
            print(f'Name is {name}, age is {age}')
        ```

        - `myfun(age=29, name='Abhishek')`   # prints "Name is Abhishek, age is 29" (mind that arguments position is different than parameters position)

    3. **Positional arguments:**

        ```python
        def myfun(name, age):
            print(f'Name is {name}, age is {age}')
        ```

        - `myfun('Abhishek', 29)`  # prints "Name is Abhishek, age is 29"

    4. **Methods vs functions:**

        - Functions are simply methods written in an script.

        - Methods are methods defined in a class, or built-in methods. Example: `[1, 2, 3].clear()`, `dict.items()`, `'jha'.capitalize()`, etc.

    5. **Docstrings:**

        ```python
        def myfun(name):
            '''
            Info: this method takes in a name, and prints it
            '''
            print(name)
        ```

        - When calling this function, the docstring is shown as a popup to help the client understand.

        - `print(myfun.__doc__)`   # `__doc__` is a dunder method. `__doc__` prints what is mentioned in the docstring.

        - `help(myfun)`     # Prints what is mentioned in the docstring.

    6. `*args` and `**kwargs`

        ```python
        def myfun(*args, **kwargs):
            print(args)     # prints a tuple (1, 2, 3)
            print(kwargs)   # prints a dictionary {'name': 'Abhishek', 'age': 29.0}
        ```

        - `myfun(1, 2, 3, name="Abhishek", age=29.0)`

        - __IMPORTANT__: When defining a function, rule for parameters is: parameters, `*args`, default parameters, `**kwargs`

- **Walrus operator (new to Python 3.8):**

    - We can assign an expression to a variable for further use.

    - Example:

        ```python
        if ((n := len(str)) > 5):
            print(str + " length is " + str(n))   # Used `n`, which is equal to `len(str)`

        def add_these_twice(num1, num2):
            n = (w := num1 + num2)
            return w + num1 + num2    # Used `w` as `num1 + num2`

        print(add_these_twice(2, 3))     # prints 10

- **Scope of a variable:**

    - Rule: 1. Checks for the local variable.

           2. Checks in the parent local variables.

           3. Checks in the global variable.

           4. Checks in built-in Python functions.

    - Examples:

        ```python
        sum = 5   # Global
        def big_sum():
            sum = 3      # Parent local
            def small_sum():
                return sum
            return small_sum()
        ```

        - `bug_sum()`   # prints 3, as it found it in the parent local

        ```python
        sum = 5
        def big_sum():
            # sum = 3
            def small_sum():
                return sum
            return small_sum()
        ```

        - `big_sum()`   # prints 5, as it found it in the global

        ```python
        # sum = 5
        def big_sum():
            # sum = 3
            def small_small():
                return sum
            return small_sum()
        ```

        - `bug_sum()`   # prints `<built-in function sum>`, as it found it as a built-in Python function :)

- **`nonlocal` keyword:**

    - As `global` is used to modify global variables inside a local scope, `nonlocal` is used to modify a parent local variable inside a child local scope.

    - Example:

        ```python
        def my_parent_local():
            local_attr = "hey"
            def my_child_local():
                nonlocal local_attr
                local_attr = "hey Ram!!!"
                print(local_attr)
            my_child_local()
            print(local_attr)
        ```

        - `my_parent_local()`   # prints `hey Ram!!!` twice  

        -  Parent local attribute got changed in the child local space.

    - Once a function finishes, all the local variables are destroyed to free up space by the garbage collector.

