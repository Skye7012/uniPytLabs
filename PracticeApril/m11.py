n=4
m=3
mtx = [ [1,2,3],
    [3,4,5],
    [6,7,8],
    [3,4,1]
]

for i in range(n):
    if(i%2==0):
        for j in range(m):
            print(mtx[i][j], end=' ')
        print()
    else:
        for j in range(m):
            print(mtx[i][-j-1], end=' ')
        print()

# for i in range(n):
#     for j in range(m):
#         print(mtx[i][j], end=' ')
#     print()