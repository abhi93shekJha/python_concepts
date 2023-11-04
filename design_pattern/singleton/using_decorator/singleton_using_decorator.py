def singleton(cls):
    instance_dict = {}    # we can access mutable objects without using "nonlocal" keyword from inner functions
    
    def get_instance(*args, **kwargs):
        if cls not in instance_dict:    # we can access this dictionary from this scope, for a variable we would have used 'nonlocal' keyword
           instance_dict[cls] = cls(*args, **kwargs)
        return instance_dict[cls]
    return get_instance

@singleton
class Singleton:
    pass

s1 = Singleton()
s2 = Singleton()

print(s1 is s2)


# Another way of creating Singleton class using local variable
def singleton_different(cls):
    instance = None
    
    def wrapper(*args, **kwargs):
        nonlocal instance
        if not instance:
            instance = cls(*args, **kwargs)
        return instance
    
    return wrapper

@singleton_different
class SingletonAliter:
    pass

s1 = SingletonAliter()
s2 = SingletonAliter()

print(s1 is s2)

