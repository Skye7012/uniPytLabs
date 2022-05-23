import pickle
FILENAME = "input.dat"
a=[]   
with open(FILENAME, "rb") as file:
    for i in range(0,10):
        x=pickle.load(file)
        a.append(x)
    print(a)
    a.reverse()
    print(a)
with open(FILENAME, "wb") as file:
    for i in range(0,10):
        pickle.dump(a[i])
