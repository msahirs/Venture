import numpy as np

FORCE_TYPES = ["Drag","Gravity"]

class Force_collection:

    def __init__(self,keys, ) -> None:

        self.validate_keys(keys)

        self.force_keys = keys

        
    def validate_keys(self,keys):

        matching = [s.base_info() for s in keys if any(xs in s.base_info() for xs in FORCE_TYPES)]
        
        if matching == [key.base_info() for key in keys]:
            print("Valid input")
        
        else:
            
            diffs = set([key.base_info() for key in keys]).difference(matching)

            print(" Invalid Input. Following values are not in database:\n", diffs)
            raise BaseException("Input Error")

    def insert_force(self,force):
        
        self.force_keys.append(force)
        self.validate_keys(self.force_keys)

    def remove_force(self,index):
    
        self.force_keys.pop(index)

    def evaluate_forces(self,t,y):

        sum = np.sum([func.eval(t,y) for func in self.force_keys])

    def print_forceSummary(self):

        for i in self.force_keys:
            print("Class type is", i.base_info(),", with ID =", i.get_ID())



class Force:
    def __init__(self, ID,) -> None:

        self.ID = ID

    @staticmethod
    def base_info():
        return "Force parent class"

    
    def get_ID(self):
        return self.ID

    def eval(self,t,y):
        pass

    
class Drag(Force):
    def __init__(self,ID) -> None:

        super().__init__(ID)

    @staticmethod
    def base_info():
        return "<Drag>"

    def eval(self, t, y):
        from drag import calculate_drag

        calculate_drag()

class Gravity(Force):
    def __init__(self, ID,) -> None:
        
        super().__init__(ID)

    @staticmethod
    def base_info():
        return "<Gravity>"

    def eval(self, t, y):
        from gravity import CONST_G

        CONST_G()


drag_1 = Drag("drag_1")
gravity_1 = Gravity("gravity_1")


a = Force_collection([drag_1, gravity_1])

a.print_forceSummary()





