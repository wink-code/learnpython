def g():
    g = (x**2 for x in range(10))
# print(type(g))
def fib(max):
    n,a,b=0,0,1
    while n<max:
        # print(b)
        yield b
        a,b = b,a+b
        n = n+1
    return 'done'

def main():
    pass

if __name__=='__main__':
    main()