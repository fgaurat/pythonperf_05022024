
def do_log(prefix=""):
    def wrapper_func(func):

        def wrapper(*args,**kwargs):
            print(f"{prefix} AVANT",func,args,kwargs)
            r = func(*args,**kwargs)
            print(f"{prefix} APRES",func,r)
            return r
        return wrapper
    return wrapper_func

# @do_log
@do_log('SAYHELLO')
#----
def say_hello(name):
    return f"Hello {name}"
#----


def main():
    r= say_hello("Fred")

    print(r)

if __name__=='__main__':
    main()
