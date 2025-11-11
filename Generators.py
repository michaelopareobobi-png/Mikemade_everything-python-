def sqr_num(n):
    n=int(input('enter number of perfect squares needed between 1 and n:'))
    i=1
    while i<=n:
        sqr=i*i
        yield sqr
        i=i+1
        if sqr > n:
            break


val=sqr_num(4)
g=[i for i in val]
g.pop(-1)
print(g)