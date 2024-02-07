def add(*p):
    """
    add 
    """
    r = 0
    for value in p:
        r+=value
    return r

# def mult2(p):
#     r = []
#     for value in p:
#         r.append(value*2)
#     return r

def mult2(v):
    return v*2

def main():

    l = [10,20,30]
    r = add(*l)
    print(r) # 60

    r = add(10,20,30)
    print(r) # 60
    l = [10,20,30,40,50]
    a,b,c,*d = l
    print(a,b,c)
    print(*l)

    l = [10,20,30]
    r = mult2(l)
    print(r) # [20,40,60]

    r = list(map(mult2,l))
    r = list(map(lambda v:v*2,l))
    print(r)


if __name__=='__main__':
    main()
