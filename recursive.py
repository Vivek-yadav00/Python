'''
#Recursion- When a function calls itself
def fact(n):
    #Base Case
    #Operation
    #Recurssive Call
    '''
def test1(n):
    if n==0:
        return
    test1(n-1)
    print(n)
test1(6)