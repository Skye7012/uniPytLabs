import string
S=input("S->")
k=0
for c in S:
    if c in string.punctuation:
        k+=1
print(k)
