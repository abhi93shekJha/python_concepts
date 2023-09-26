def make_it_jaguar(cls):
    # adding class variables
    cls.type = "Jaguar"
    
    original_method = cls.car_speed
    # modifying the existing MyCar class method
    def modified_method(self, speed):
        print(f"Current speed: {speed}km/s")
        print("Adding speed for Jaguar")
        speed += 100
        result = original_method(self, speed)
        print("Speed modification completed!!")
        return result
        
    cls.car_speed = modified_method
    return cls


@make_it_jaguar
class MyCar:
    
    def __init__(self, color):
        self.color = color
        
    def car_speed(self, speed):
        print(f"The {self.color} Jaguar speed is {speed} km/s!!")
        
if __name__=="__main__":
    car1 = MyCar("Red")
    car1.car_speed(150)
    
    car2 = MyCar("White")
    car2.car_speed(100)
    
    MyCar.type = "Jaguar Modified"  # making static behavious of a variable
    
    print(f"class variable1 is {car1.type}")
    print(f"class variable2 is {car2.type}")