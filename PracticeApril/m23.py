n=4
m=3
mtx = [ [1,2,3],
    [3,4,5],
    [6,7,8],
    [3,4,1]
]
res=[]

for i in range(n):
    res.append(min(mtx[i]))

for i in range(n):
    print(res[i])

# for i in range(n):
#     for j in range(m):
#         print(mtx[i][j], end=' ')
#     print()