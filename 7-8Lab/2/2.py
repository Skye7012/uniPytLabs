path = "7-8Lab/2/dates.txt"
pathM = "7-8Lab/2/monhts.txt"
pathY = "7-8Lab/2/years.txt"

with open(path, 'r') as file:
	dates = file.readlines()
	
with open(pathM, 'w') as fileM:
	with open(pathY, 'w') as fileY:
		mY = list(map(lambda x : x.split('/')[1:3], dates))
		fileM.write('\n'.join([i[0] for i in mY]))
		fileY.write(''.join([i[1] for i in mY]))

print('done')