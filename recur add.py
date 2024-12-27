def sm(a,b):
    if a==0:
        return b
    else:
        return 1 + sm(a-1,b)
a=20
b=12
res=sm(a,b)
print(res)