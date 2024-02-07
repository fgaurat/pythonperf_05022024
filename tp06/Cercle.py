import math
from ICalcGeo import ICalcGeo

class Cercle(ICalcGeo):

    def __init__(self,rayon=0) -> None:
        self.__rayon = rayon


    @property
    def rayon(self):
        return self.__rayon
    
    
    @rayon.setter
    def prop(self,rayon):
        self.__rayon = rayon

    @property
    def surf(self):
        return self.__rayon**2*math.pi
    

