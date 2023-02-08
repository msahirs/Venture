import numpy as np

FORCE_TYPES = ["drag","gravity"]

class Force_collection():

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


class Drag():
    def __init__(self, ID,) -> None:
        pass

    @staticmethod
    def base_info():
        return "drag"

class Gravity():
    def __init__(self, ID,) -> None:
        pass

    @staticmethod
    def base_info():
        return "gravity"


Force_collection([Drag("drag_1"), Gravity("gravity_1")])