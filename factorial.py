n= int(input("Enter the no. whose factorial u want to find:"))

def fac(n):
    a=1
    for i in range(1,n+1):
        a=a*i
    return a

result=fac(n)
print(result)