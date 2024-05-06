import sys
from random import random as randf

print( "Методическое умножение (подвижного метода)" )

#(a, b) = (2518, 3571)
#(a, b) = (123456789, 11111)
#(a, b) = (123456789123456789, 11111111111111)
#(a, b) = (22, 331)

if len( sys.argv ) == 3:
	a = int(sys.argv[1])
	b = int(sys.argv[2])
	print(f'a = {a}\nb = {b}\n')
else:
	if len( sys.argv ) != 1:
		print( "Incorrect arguments usage, should be \"{sys.argv[0]} A B\"." )

	a = int(input( "a = " ))
	b = int(input( "b = " ))



if randf() < 0.5:
	print( f'Пусть перевёрнутое A ({a}) будет вверху:' )
else:
	print( f'Пусть перевёрнутое B ({b}) будет вверху:' )
	(a, b) = (b, a)


alist = [int(digit) for digit in str(a)][: : -1]
blist = [int(digit) for digit in str(b)]

alen = len( alist )
blen = len( blist )
apos = blen - 1
bpos = 0	# In range [0..bothlen).
bothlen = apos + alen
minlen = min( alen, blen )
reslist = list( [0] * bothlen )
prevoverflow = 0

visualbothlen = alen + blen * 2

while ( bpos < bothlen ):
	reslen = (bothlen - bpos - 1)
	result = prevoverflow
	visualoper = ""

	for i in range( min( minlen, bothlen - bpos, bpos + 1 ) ):
		aindex = max( 0, i + max( 0, bpos - blen + 1 ) )
		bindex = max( 0, blen - bpos - 1 ) + i

		result += alist[ aindex ] * blist[ bindex ]
		visualoper += f"{alist[ aindex ]}*{blist[ bindex ]} + "
		#print( f"{i}. result += {alist[ aindex ]} [{aindex}] * {blist[ bindex ]} [{bindex}] == {result}, bpos {bpos}" )

	if ( prevoverflow != 0 ):
		visualoper = f"{prevoverflow} + " + visualoper

	visualoper = visualoper[ : -3 ] + f" = {result}"

	reslist[ reslen ] += result % 10
	prevoverflow = result // 10

	print( (' ' * apos), *alist, '\n',
		   (' ' * bpos), *blist, '\n', ('─' * visualbothlen), f' ({visualoper}, перенос {prevoverflow})\n',
		   (' ' * apos), *reslist[reslen : ], '\n', sep='' )

	bpos += 1


print( f"Сравнение с обычным перемножением: {a * b}." )
