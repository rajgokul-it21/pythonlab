a=[1,2,3,4,5]
for i in range(5):
    temp=a[0]
    for j in range(4):
          a[j]=a[j+1]
    a[4]=temp 
    print(a)
