# Advance Python concepts notes and example codes
### I have explained most of the advance python concepts in simple terms for clear understanding.

## Miscellaneous Concepts
### pdb (Python Debugger)
- import pdb, we can debug using terminal.
- pdb.set_trace(), we add this method, whereever we want to stop the debugger.
- this is same as using debugger in an IDE.
- from terminal, when in debugging environment, we can add commands like,
- step (moves to next line and executes the previous line of code)
- a (list out all the variables, till the executed code)
- we can assign a variable, a different value
- help (list out all the commands available)
- help any_command (gives details about any command)

### type hint uses '->', ':'
- We can show the expected type of variables, parameters, or return types.
- Not used at runtime, for code understanding and documentation purpose only.
```python

# Example 1:
def add_numbers(x: int, y: int) -> int:
    return x + y

# Example 2:
age: int = 25

# Example 3:
from typing import List, Dict
def process_data(data: List[int]) -> Dict[str, int]:
    # Function logic

```
