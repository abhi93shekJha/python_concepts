class Singleton:
    __instance = None
    def __init__(self) -> None:
        raise RuntimeError("Cannot create instance of a singleton class!!")
    
    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = cls.__new__(cls)
        return cls.__instance
    
s1 = Singleton.get_instance()
s2 = Singleton.get_instance()
print(s1 is s2)        
