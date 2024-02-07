import sys 

# TypeError : UpperCamelCase / PascalCase
# typeError : camelCase
# type_error : snake_case
# type-error : kebab-case





def main():
    a = 2
    print(a)
    print(hex(id(a)))
    
    a = 3123456423
    print("getrefcount",sys.getrefcount(3123456423))
    print(a)
    print(hex(id(a)))

    b = 3123456423
    print("getrefcount",sys.getrefcount(3123456423))
    print(b)
    print(hex(id(b)))
    # a = 12

    s = "Toto"
    s[0] = "o"



if __name__=='__main__':
    main()


