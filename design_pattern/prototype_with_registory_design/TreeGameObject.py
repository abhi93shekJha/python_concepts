from . import GameObject, Clonable
import copy

class TreeGameObject(GameObject, Clonable):
    def __init__(self, x, y, pixels, shape):
        super().__init__()
        self.x = x
        self.y = y
        self.pixels = pixels
        self.shape = shape
        
    def create_tree(self):
        print(f"Using {self.shape} to create the tree")    
   
    def clone(self):
        return copy.deepcopy(self)     
        