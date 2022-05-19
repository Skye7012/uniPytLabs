a=[]
b=[]
m=int(input())
n=int(input())

for j in range(m):
    x=int(input())
    b.append(x)

for i in range(n):
    a.append(b)

print()
print(b, 'is b')
print(a, 'is a')

for i in range(n):
    for j in range(m):
        print(a[i][j], end=' ')
    print()