from RectangleSingleton import RectangleSingleton
from Rectangle import Rectangle


def main():
    r1 = RectangleSingleton(2,7)
    r2 = RectangleSingleton(5,8)
    r3 = Rectangle(2,7)
    r4 = Rectangle(5,8)
    print(hex(id(r1)))
    print(hex(id(r2)))
    if id(r1) == id(r2):
        print("RectangleSingleton ok")
    else:
        print("RectangleSingleton ko")

    if id(r3) == id(r4):
        print("Rectangle ok")
    else:
        print("Rectangle ko")



    print(r1.longueur)
    print(r2.longueur)
    print(r3.longueur)
    print(r4.longueur)
    # r1.longueur=12
    # print(r1.longueur)
    # print(r2.longueur)

    # print(type(r1))
    # print(type(r2))
    
    # print(type(RectangleSingleton))


if __name__=='__main__':
    main()
