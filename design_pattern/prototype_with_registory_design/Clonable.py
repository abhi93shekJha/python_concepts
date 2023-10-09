from abc import ABC, abstractmethod

class Clonable(ABC):
    @abstractmethod
    def clone(self):
        ...