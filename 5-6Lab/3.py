semestr = input("Введите номер семестра: ")

if(semestr.isdigit() and len(semestr) == 1):
	semestr = int(semestr)
	
	match semestr:
		case 1 | 2 : print("1 Курс")
		case 3 | 4 : print("2 Курс")
		case 5 | 6 : print("3 Курс")
		case 7 | 8 : print("4 Курс")
		case _ : print("Не бывает такого семестра")

else:
	print("Введите НОМЕР семестра!!!")
