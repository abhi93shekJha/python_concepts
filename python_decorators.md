# Decorators
- Adds extra functionality to a method.
- Very helpful, use cases can be, we can write a generic decorator that calculates time complexity of functions. Shown in the example below.
- Let's say, we want to capture some event, for example if someone logs in, we want to save that user info when authenticate function runs, we can use decorator then.
- We can capture events for analytics purposes.
```python
from time import time
def performance(fun):
  # as you can imagine, *args and **kwargs can accept any arguements
  def wrapper(*args, **kwargs):
    start = time()
    fun(*args, **kwargs)
    end = time()
    print(f"Time taken: {end-start} sec")
  return wrapper  

@performance
def do_complex_calculation(num):
  for i in range(10000):
    i*20
  print(num)

do_complex_calculation(20)

# Use of decorators hides the below code
wrapper = performance(do_complex_calculation) # perfomance function returned a wrapper function
wrapper(20)
```
