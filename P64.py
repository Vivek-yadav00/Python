def fibb(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fibb(n-1)+fibb(n-2)
n=4
for i in range(n):
    print(fibb(i))
