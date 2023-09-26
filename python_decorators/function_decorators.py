
def my_decorator(fun):
    def wrapper(*args, **kwargs):
        print("Don't forget to add salt")
        result = fun(*args, **kwargs)
        print("Please add spices too!!")
        return result
    return wrapper

@my_decorator
def cook_food(vegetables, cereals, spicy=False):
    print(f"Cooking food using {vegetables} using {cereals}", end=" ")
    if spicy:
        print("It should be spicy")
                
        
def main():
    cook_food("Potato", "Rice", True)
    
if __name__=="__main__":
    main()
        