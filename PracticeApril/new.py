a=[]
n=int(input())
m=int(input())

for i in range(n):
    b=[]
    for j in range(m):
        b.append(i*10)
    a.append(b)

for i in range(n):
    for j in range(m):
        print(a[i][j], end=' ')
    print()