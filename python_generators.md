# Generators in python
- For faster iteration. Faster because they only compute next value when requested.
- range(100) is created using generator. I have created a custom range below for understanding.
- A generator is always an iterator, an iterator may or may not be a generator (for example list, or tuple are not generators).
- A generator is created using "yield" keyword. "yield" pauses the current function and returns the current value, when next is called on that function.
- Using "yield" keeps only the current value in the memory forgetting about previous values, making it no space consuming and faster as compared to using a list or other similar data structures.
- Example of a generator is shown below.
### Note:
- for i in range(100), here, this for loop internally calls next() on the range generator one after another.
- Also, for loop stops as soon as StopIteration is thrown by range generator under the hood.
### Example
```python
def generator(num):
  for i in range(num):
    yield i

my_generator = generator(20)
next(my_generator)
next(my_generator)
print(next(my_generator))

my_generator = generator(1)    # only for 1
next(my_generator)
next(my_generator)    # next() will output 'StopIteration' error

# calls next and stops on StopIteration thrown by next() implicitly
for i in generator(10):
  print(i)

# Here yield is pausing the function and only returning next value on calling next(on function).
```
### Custom range implemented below
```python
class CustomRange:
  current = 0
  def __init__(self, start, end):
    self.start = start
    self.end = end
    CustomRange.current = self.start-1

  # will override __iter__ dunder method, to make it behave like an iterator
  def __iter__(self):
    return self

  def __next__(self):
    if CustomRange.current < self.end-1:
      CustomRange.current += 1
      return CustomRange.current
    raise StopIteration  

range = CustomRange(2, 10)
# Below for loop calls next() method and stops when next() throws StopIteration exception.
for i in range:
  print(i)
# OR
for i in CustomRange(0, 10):
  print(i)
```
### fibonacci with Generator, takes less space and have better time complexity than using any other data structure (list or tuple)
```python
def fibonacci_generator(num):
  a = 0
  b = 1
  for i in range(num):
    yield a
    temp = a
    a = b
    b = temp + b

for i in fibonacci_generator(10):
  print(i)
```

