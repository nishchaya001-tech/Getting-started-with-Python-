a=[2,5,4,9,6]
n=len(a)

def bubble(a):
    for i in range(n):
        for j in range(0,n-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return a

b=bubble(a)
print(b)