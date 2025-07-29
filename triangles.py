def triangle(max):
    n,ls = 1,[1]
    yield [1]
    # if n<max:
    while n<max:
        Ls = [1]
        # L = [1]+[L[i]+L[i+1] for i in range(len(L)-1)]+[1]
        for k in range(len(ls)-1):
            Ls.append(ls[k]+ls[k+1])
        Ls.append(1)
        yield(Ls)
        ls = Ls
        n += 1
    return 'done'

def main():
    t = triangle(5)
    while True:
        try:
            x = next(t)
            print(x)
        except StopIteration as e:
            print('Generator return value:',e.value)
            break

if __name__=='__main__':
    main()