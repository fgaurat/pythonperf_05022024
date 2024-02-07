from collections import deque
def main():
    l = [10,20,30]
    print(l)
    l.append(40)
    print(l)
    last = l.pop()
    print(l)
    print(last)

    l.insert(0,1000)
    print(l)
    first = l.pop(0)
    print(l)
    print(first)

    d = deque(l)

    d.appendleft(1000)
    print(l)
    print(d)




if __name__=='__main__':
    main()
