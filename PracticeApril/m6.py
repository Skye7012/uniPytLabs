a=[]
b=[]
print('print n')
n=int(input())
print('print m')
m=int(input())
print('print q')
q=int(input())

for j in range(m):
    x=int(input())
    b.append(x)

print(b, 'is b')
a.append(b)
print(a, 'is a')

for i in range(1,n):
    b2=[]
    for j in range(m):
        b2.append(a[i-1] * q)
    a.append(b)
    print(b2, 'is b2')
    print(a, 'is a')



print()
print(b, 'is b')
print(a, 'is a')

for i in range(n):
    for j in range(m):
        print(a[i][j], end=' ')
    print()