from Rectangle import Rectangle
from DataRectangle import DataRectangle

def main():
    r = Rectangle(2,3)
    r1 = Rectangle(2,3)
    s = str(r)
    print(s)

    if r==r1:
        print("ok")
    else:
        print("ko")

    print(Rectangle.cpt())
    

    r3 = Rectangle.buildFromStr("12x58")
    # r3.toto = 22

    # print(r3.__dict__)
    
    print(50*'-')
    dr = DataRectangle(5,9)
    dr1 = DataRectangle(5,9)

    print(dr)
    print(dr1)
    if (dr==dr1):
        print("ok")
    else:
        print("ko")





if __name__=='__main__':
    main()
