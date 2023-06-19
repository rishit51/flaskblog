def cyclic(a):
    for i in range(len(a)):
       correct=a[i]-1
       if(a[i]!=a[correct]):
           a[i],a[correct]=a[correct],a[i]

a=[5,4,3,2,1]

cyclic(a)
print(a)