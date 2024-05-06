import sys

print( "Русское умножение" )

#(a, b) = (2518, 3571)

if len( sys.argv ) == 3:
	a = int(sys.argv[1])
	b = int(sys.argv[2])
	print(f'a = {a}\nb = {b}\n')
else:
	if len( sys.argv ) != 1:
		print( "Incorrect arguments usage, should be \"{sys.argv[0]} A B\"." )

	a = int(input( "a = " ))
	b = int(input( "b = " ))

(origa, origb) = (a, b)

if ( a > b ):
	(a, b) = (b, a)


def lenstr( expr ) -> int:
	return len( str( expr ) )

def rjust( var, justifylen: int, justifychar: str = ' ' ) -> str:
	return str( var ).rjust( justifylen, justifychar )


def get_right_column() -> str:
	global a, llen
	return ( rjust( a, llen ) + ' │' )

def get_left_column() -> str:
	global b, rlen, a
	return ( rjust( b, rlen ) if ( a & 1 ) else rjust( b, rlen, '─' ) + '─ (число "a" чётное)' )


rlen = lenstr( a * b ) + 1
llen = lenstr( a ) + 1
rsumlist = [ b ] if a & 1 else []

# Digits A and B:
print( get_right_column(), end='' )
print( get_left_column(), end='' )
# Separator:
print( '\n ' + '─' * llen + '┼' + '─' * rlen, sep='' )


while a > 1:
	a //= 2
	b *= 2

	if ( a & 1 ):
		rsumlist += [ b ]

	print( get_right_column(), get_left_column(), sep='' )


rresult = sum( rsumlist )

# Separator 2:
print( (' ' + '─' * llen + '╪' + '═' * rlen + '\n') + rjust( rresult, llen + rlen + 2 ) )

outresstr = 'Ответ: ' + ' + '.join( map( str, rsumlist ) ) + f' = {rresult}'
print( '\n' + outresstr + '\n' + rjust( f'(Обычное умножение: {origa * origb}).', len( outresstr ) + 2 ) )

