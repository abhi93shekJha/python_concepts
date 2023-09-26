import time

def timing_decorator(fun):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = fun(*args, **kwargs)
        end = time.time()
        print(f"Time take is {end-start}")
        return result
    return wrapper

@timing_decorator
def calculate_cube(val):
    return val*val*val

cube = calculate_cube(100000)
print("cube is " + str(cube))