# n=int(input("no. of rows"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

# n=4
# s=n-1
# k=1
# for i in range(1,n):
#     for j in range(1,i+1):
#         print(s*" ",k*"*",end=" ")
#         print()
#         k+=2
#         s-=1
# n=7
# k=ord('A')
# print(k)

# for i in range(1,n):
#     for l in range(1,i+1):
#         print(chr(k),end=" ")
#         k+=1
#     print()

# n=4
# k=1
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(k,end=" ")
#         k+=1
#     print()


# r=int(input("rows: "))            Pascal triangel
# for n in range(0,r):
#     for m in range(r,n,-1):
#         print(' ',end='')
#     c=1
#     for r in range(0,n+1):
#         print("%d "%c,end=" ")
#         c=c*(n-r)/(r+1)
#     print()

n=int(input("Enter number:"))
t=n
r=0
while(n>0):
    d=n%10
    r=r*10+dig
    n=n//10
if(t==r):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")