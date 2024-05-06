import sys

print( "Рачинский-Ⅰ" )

if len( sys.argv ) == 3:
	n = int(sys.argv[1])
	p = int(sys.argv[2])
	print(f'n = {n}\np = {p}\n')
else:
	if len( sys.argv ) != 1:
		print( "Incorrect arguments usage, should be \"{sys.argv[0]} N P\"." )

	print( "Число, простой делитель:" )
	n = int(input( "n = " ))
	p = int(input( "p = " ))

#(n, p) = (32451, 181)
#(n, p) = (24791, 101)


slen = len( str( p ) ) - 1

s = list(tuple())
print()

for i in range( 1, slen + 1 ):
	a = int( str( p )[ : i] )
	b = int( str( p )[i : ] )
	print( f"При s = {i}: a = {a}, b = {b}" )
	s.append( (slen + 1 - i, a, b) )


cur = n
print()



def getmk( digit: int, klen: int ) -> tuple:
	m = digit // (10 ** klen)
	k = digit % (10 ** klen)

	return (m, k)

def step( digit: int, klen: int, a: int, b: int ) -> float:
	m = digit // (10 ** klen)
	k = digit % (10 ** klen)

	print( f"    {m}*{b} - {k}*{a} " )

	return m * b - k * a


while cur > p:
	reslist = list()
	m = 0
	k = 0
	
	for i in s:
		(m, k) = getmk( cur, i[0] )
		(a, b) = (i[1], i[2])

		res = m*b - k*a
		print( f"При s = {i[0]}:" )
		print( f"  {m}╲{k}, где m={m}, k={k}" )

		if ( res < 0 ):
			res = -res
			print( "  При делении по модулю знак не учитывается." )
			print( f"  mb - ka = |{m}*{b} - {k}*{a}| = {res}" )
		else:
			print( f"  mb - ka = {m}*{b} - {k}*{a} = {res}" )

		reslist.append( res )

		if ( res <= p ):
			break


	cur = min( reslist )
	if ( cur > p ):
		print( f"Далее раскладываем {cur} (как минимальное).\n",  )


print( f"\nОтвет: {n}/{p}", "(не делится)." if ( n % p != 0 ) else "(делится)." )
