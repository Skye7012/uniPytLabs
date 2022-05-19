a=[]
n=int(input("12123:"))
m=int(input("123123:"))

for i in range(n):
    b=[]
    x=int(input("x:"))
    for j in range(m):
        b.append(x)
    a.append(b)

print()
print(a)
print(b)

for i in range(n):
    for j in range(m):
        print(a[i][j], end=' ')
    print()