a=[]
b=[]
n=int(input())
m=int(input())
d=int(input())

for i in range(n):
    b=[]
    x=int(input())
    for j in range(m):
        b.append(x+j*d)
    a.append(b)

print()
print(b, 'is b')
print(a, 'is a')

for i in range(n):
    for j in range(m):
        print(a[i][j], end=' ')
    print()