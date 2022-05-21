n=int(input("n->"))
S=input("S->")
S=S.strip() #удалить лишние пробелы
m=len(S)
if m>n:
	S=S[m-n:]
else:
	S = S.rjust(n,'.')
print(S)
