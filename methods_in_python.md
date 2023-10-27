
## Functions in python:

1. ex-
def my_function(parameter1, parameter2):
    		# Function code here

2. If no return statement, it returns null implicitly.

3. Variables defined inside a function have scope local to the function, unless defined global.

4. Lambda function - for simple operations,
	eg.- square = lambda x: x * x
	
5. default parameters: eg. = def myfun(a, b=10) #will be used if no arguement for b is passed to the funtion.

6. keyword arguments:
	eg - greet(name="Alice", age=25)
	
7. Using *args and **kwargs: to accept variable number of positional and keyword arguments.
		
	    def add(*args):
            result = 0
            for num in args:
                result += num
            return result

        total = add(1, 2, 3, 4)  # total will be 10
        
        
        def process_data(**kwargs):
    	    for key, value in kwargs.items():
              print(f"{key}: {value}")

        process_data(name="Alice", age=25, city="New York")


8. Using Functions as Variables:
   (i) Assigning Functions to Variables:
   
   	    def say_hello():
    	    print("Hello!")

        greet = say_hello  # Assign the function to another variable
        greet()  # Calls the function through the 'greet' variable

        (ii) Passing Functions as Arguments:
        
        def apply(func, x):
            return func(x)

        def square(x):
            return x * x

        result = apply(square, 5)  # result will be 25
	
    (iii) Returning Functions from Functions: used for closure and decorator
    
    	def create_multiplier(factor):
    	    def multiplier(x):
               return x * factor
            return multiplier

        double = create_multiplier(2)
	    result = double(5)  # result will be 10
		
		
9. Callback Functions:
    
    It is a function that is passed to another function, and is executed within or after the execution of that function.
    
    Very helpul in providing decoupling, flexibility and reusability.
    
    Example-
    
        def sort_and_callback(input_list, callback=None):
            sorted_list = sorted(input_list)
    
            if callback is not None:
                callback(sorted_list)

        def print_sorted_list(sorted_list):
            print("Sorted List:", sorted_list)

        def sum_sorted_list(sorted_list):
            total = sum(sorted_list)
            print("Sum of the Sorted List:", total)

        def find_max_sorted_list(sorted_list):
            max_value = max(sorted_list)
            print("Maximum Value in the Sorted List:", max_value)

        numbers = [3, 1, 2, 4, 5]

        # Use the sorting function with different callback functions
        sort_and_callback(numbers, print_sorted_list)
        sort_and_callback(numbers, sum_sorted_list)
        sort_and_callback(numbers, find_max_sorted_list)
    

10 Closure functions:
	
    A concept where a function is enclosed inside a function. Function that are used inside a function and uses the variables of enclosing function.
    
    Example-
    
    def outer_function(x):
        # This is the enclosing (or outer) function
        def inner_function(y):
            # This is the enclosed (or inner) function
            return x + y

        # Return the inner function, creating a closure
        return inner_function

    # Create a closure by calling the outer function with a value for 'x'
    closure = outer_function(10)

    # Use the closure with a value for 'y'
    result = closure(5)
    print(result)  # Output: 15
    
    (i) Used for Factory functions: giving multiplier on demand.
    
        def create_multiplier(factor):
    	    def multiplier(x):
                return x * factor
            return multiplier

	    double = create_multiplier(2)
	    triple = create_multiplier(3)

	    result1 = double(5)  # result1 will be 10
	    result2 = triple(5)  # result2 will be 15
	    
     (ii) Used for data hiding: Example:
     
         def counter():
             count = 0  # Encapsulated data

             def increment():
                 nonlocal count
                 count += 1
                 return count

             return increment

         counter1 = counter()
         counter2 = counter()

	 count1 = counter1()  # count1 is 1
	 count2 = counter1()  # count2 is 2
	 count3 = counter2()  # count3 is 1
	 
     (iii) Managing States: See in example, that when running count2, count state remains 1. And for count3, count resets again.
     
          def stateful_counter():
    	      count = 0  # Initial state

    	      def increment():
                  nonlocal count
        	  count += 1
              return count

              return increment

	   counter = stateful_counter()

	   count1 = counter()  # count1 is 1
	   count2 = counter()  # count2 is 2
	   count3 = counter()  # count3 is 3
		 
   



		

	

# Decorators

1. Function Decorators: additional functionality to an existing function.


## Usage/Examples

```python
# Decorator function
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result
    return wrapper

# Function with arguments and parameters
@my_decorator
def greet(name, message):
    return f"Hello, {name}! {message}"

result = greet("Alice", "Have a great day.")
print(result)

```


## Class Decorators:

- Adds extra instance variables, methods to an existing class.
- The extra attributes and behaviours get added when the class is defined or loaded.
- Modifies an existing method as well.

More information in the code.


