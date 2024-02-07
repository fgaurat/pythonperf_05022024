import traceback


def div(a,b):
    return a/b

def call_div(a,b):
    r=0
    try:
        print("ouverture du fichier")
        r = div(a,b)
    finally:
        print("fermeture du fichier")
    return r

def main():
    a = 2
    b = 0
    try:
        # c = b/a
        c = call_div(a,b)
        print(c)
        #...
    except Exception as e:
        print(e)
        # traceback.print_exc()
    else:
        print("pas d'erreur !")

    finally:
        print("finally")

    print("Après")


if __name__=='__main__':
    main()
