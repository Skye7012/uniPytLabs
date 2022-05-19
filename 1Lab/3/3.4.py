from statistics import mean

n = int(input("n = "))
students = []
neu = 0
avg = []

for i in range(n):
	print("Оценки ",i+1, " ученика")
	temp = []
	for j in range(4):
		temp.append(int(input("\t" + str(j+1) + " оценка = ")))
	students.append(temp)

for student in students:
	if(1 in student or 2 in student or 3 in student):
		neu+=1
	avg.append(mean(student))
avg = mean(avg)


print("Неуспевающих = ", neu)
print("Средний балл группы = ", avg)