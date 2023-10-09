from .GameObject import GameObject
from .Clonable import Clonable
import copy

class CarGameObject(GameObject, Clonable):
    
    def __init__(self, x, y, pixels, shape):
        super().__init__()
        self.x = x
        self.y = y
        self.pixels = pixels
        self.shape = shape
        
    def create_car(self):
        print(f"Using {self.shape} to create the car")    
    
    def clone(self):
        return copy.deepcopy(self)    