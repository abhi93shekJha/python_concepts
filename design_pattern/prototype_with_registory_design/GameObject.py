from abc import ABC

class GameObject(ABC):
    
    def __init__(self) -> None:
        self.x = None
        self.y = None
        self.pixels = None
    
    def position_object(self):
        print(f"Placing it at {self.x}, {self.y}")