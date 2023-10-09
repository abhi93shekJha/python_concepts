import WrongPizza

class Main:
    def make_pizza_with_type(self, pizza_type):
        if pizza_type == 'corn':
            print("Making corn pizza")
        elif pizza_type=='cheeze':
            print("making cheeze pizza")
        elif pizza_type=='onion':
            print("Making onion  pizza")
        else:
            raise WrongPizza("Unknown type!!")     
        
if __name__=="__main__"        