letters = {
	'Й':1, 'Ц':2, 'У':3, 'К':4, 'Е':5, 'Н':6, 'Г':7, 'Ш':8,
	 'Щ':9, 'З':10, 'Х':11, 'Ъ':12, 'Ф':13, 'Ы':14, 'В':15, 'А':16,
	 'П':17, 'Р':18, 'О':19, 'Л':20, 'Д':21, 'Ж':22, 'Э':23, 'Я':24,
	 'Ч':25, 'С':26, 'М':27, 'И':28, 'Т':29, 'Ь':30, 'Б':31, 'Ю':32,
	 'Ё':5,
}

name = input('Фамилия Имя (пробелы и повторы букв удалятся): ')
name = name.upper()
name = "".join(dict.fromkeys(name)).replace(' ','')
if len(name)==0:
	print("Строки нет")
	exit(1)
elif len(name)<6:
	print("Короткая строка (минимум 6 символов), зациклена")
	name = name * 6

name = name[:6]

print(f'Для "{name}":')

n, w, v = [None]*6, [None]*6, [None]*6

for i, ch in enumerate(name):
	code = letters.get(ch)
	#print(ch, code)
	if code is not None:
		n[i] = code
		w[i] = (code%8)+1
		for div in range(code, 33+8):
			if div%w[i] == 0:
				v[i] = div
				break
		if v[i] is None:
			print(f'v[{i}] не может быть найдена. Выход за теоретический предел подбора')
			exit(2)
	else:                
		print(f'Пропуск "{ch}"')

def printlist(title, lst):
	print(title, end='')
	for i in lst: print(i, end=' ')
	print()

printlist('n: ', n)
printlist('w: ', w)
printlist('v: ', v)
