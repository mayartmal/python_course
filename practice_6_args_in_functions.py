

def printab(a, b, *args):
    print('positional arg a: ', a)
    print('positional arg b: ', b)
    print('additional args: ')
    for arg in args:
        print(arg)

printab(1, 2, 3, 4, 5, 6, 7, 8)

