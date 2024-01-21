# Error Handling in python
- As we know exception is something that is intended to be caught at runtime and error is a more broader term which include exceptions and may terminate the complete program at once.
- Python Errors - These are caught at the time of compilation and the code never runs (SyntaxError, IndentationError).
- Python Runtime errors (Exceptions) - These are thrown at runtime by programmer (CustomExceptions) or by interpreter (ValueError, TypeError, ZeroDivisionError) and handled by try, catch.
- Unlike Java, all the errors and exceptions inherits from BaseException, Exception class is a subclass of BaseException. RuntimeError and rest of the classes all inherit from Exception.
- finally block always runs.
### Notes:
- ValueError is raised by python functions or by our functions when there is an issue with the argument. Ex. int("dsf")
- We raise it using "raise ValueError("error message")".
### Examples
```python

def divide_digits(num1, num2):
  return num1 / num2

# divide_digits(1, '4') # TypeError
# divide_digits(1, 0)  # ZeroDivisionError

# SyntaxError
# def divide_digits(num1, num2)
#   return num1 / num2

# NameError (because new_name is not defined)
# def divide_digits(num1, num2):
#   return num1 / new_name

# def print_list(li):
#   print(li[4])  # IndexError

# print_list([1,2,3])

# def use_dict(di):
#   print(di['random_key'])  # KeyError
# use_dict({"hi":1})  
```
### Example using try, except, else and finally
- Always except specific errors, otherwise we will miss out of the actual error generated.
- For example, if we except Exception for TypeError, we will not be able to catch and log ZeroDivisionError.
```python
while True:
  user_input = input("Please enter your age.")
  try:
    age = int(user_input)
    10/age
  except ValueError:
    print("Please enter a number.")
  except ZeroDivisionError:
    print("Age should be greater than 10")
  else:
    print("This runs if except do not run")
    break
  finally:
    print("This finally block always run")
    print("Even if while loop breaks in else block")
    print("It can only be used with try also")
```
### We can also except and raise an error in below way
```python
while True:
  user_input = input("Please enter your age.")
  try:
    age = int(user_input)
    10/age
    raise ValueError("Wrong age provided")
  except (ZeroDivisionError, ValueError) as err:
    print(err)
```
