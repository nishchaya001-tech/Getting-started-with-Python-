list=[2,5,4,9,6]
n= int(input('Enter the no. u wanna find:'))


def finder(list,n):
    m=0
    for i in list:
        m+=1
        if i==n:
            print("No. found in the position:", m)
            

finder (list,n)