class SingletonMeta(type):
    __instance = None
    def __call__(self, *args, **kwargs):
        # important: self is actually a class object which this metaclass is creating
        if self.__instance is None:
            self.__instance = super(SingletonMeta, self).__call__(*args, **kwargs)
        return self.__instance    
        
        
class Singleton(metaclass=SingletonMeta):
    pass

s1 = Singleton()
s2 = Singleton()

print(s1 is s2)