from Cercle import Cercle
from Rectangle import Rectangle
from ICalcGeo import ICalcGeo

def show_surface(o:ICalcGeo):
    print(o.surface)

def main():
    re = Rectangle(2,5)
    ce = Cercle(2)
    print(ce.surface)
    print(re.surface)
    show_surface(re)
    show_surface(ce)

if __name__=='__main__':
    main()
