def make_inc(v):
    l = [i for i in range(5)]
    def do_inc(vi):
        print(l)
        return v+vi

    return do_inc

def main():
    inc = make_inc(12)
    r = inc(5)
    r = inc(12)
    r = inc(74)
    r = inc(8)
    print(r) # 17

if __name__=='__main__':
    main()
