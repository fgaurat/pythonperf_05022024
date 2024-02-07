import copy

def main():
    l = [10,20,30,40,50]
    print(l[1:4]) # [1:4[
    
    print(l[-1])

    print(l[:3])
    print(l[3:])
    print(l[:])

    l1 = l[:]
    l[0] = 1000
    print(l)
    print(l1)

    l2 = [
        [10,20,30],
        [40,50,60],
        [70,80,90],
    ]

    print(l2)
    # l3 = l2[:]
    # l3 = copy.copy(l2)
    l3 = copy.deepcopy(l2)
    l3 = l2.copy()
    
    l2[1][1] = 1000

    print(l2)
    print(l3)





if __name__=='__main__':
    main()
