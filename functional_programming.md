- Simply put, in functional programming we keep data and functions separated from each other.
- The basic pillar of functional programming are pure functions.
- Pure functions are functions that do not interact with outside world, i.e. printing something to console or changing any variable out of its own scope.
- It should work on local variables and return the required output and should not change anything outside of it's scope.
- Writing pure functions in a bigger project helps reduce errors.
### Map
```python
# this is pure function
def square(item):
  return item*item

my_list = [1, 2, 3]
# map will work on every element of the list
new_list = list(map(square, my_list))
print(new_list) # prints, [1, 4, 9]
# original list won't change, because of pure function
print(my_list) # prints, [1, 2, 3]


# method used for filter should always return boolean
def filter_even(item):
  return item%2==0

my_list = [1, 2, 3, 4, 5, 6]
# as the name suggests, it will filter out items from a list
new_list = list(filter(filter_even, my_list))
print(new_list)  # prints, [2, 4, 6]
# original list won't change, because of pure function
print(my_list)  # prints, [1, 2, 3, 4, 5, 6]


list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
list3 = (9, 10, 11, 12)  # any iterable

print(list(zip(list1, list2, list3)))
# prints, [(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]

# reduce
# it takes in an iterable, and reduce it to a value
from functools import reduce

def accumulator(acc, item):
  # acc changes with every item, 0, (0+1), (1+2), (3+3), 
  # (6,4), (10,5), (15,6)
  return acc + item

my_list = [1, 2, 3, 4, 5]
      # function  , iterable, start number (not index)  
result = reduce(accumulator, my_list, 0)  # 0 is default too
print(result)  # prints, 15

```
