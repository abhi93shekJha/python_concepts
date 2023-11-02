from using_module import singleton_module as s

singleton1 = s.Singleton()
singleton2 = s.Singleton()

print(singleton1 is singleton2)   # prints True
