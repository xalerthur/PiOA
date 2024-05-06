import sys

print( "Метод Паскаля" )

if len( sys.argv ) == 3:
	v = int(sys.argv[1])
	mod = int(sys.argv[2])
	print(f'v = {v}\nmod = {mod}\n')
else:
	if len( sys.argv ) != 1:
		print( "Incorrect arguments usage, should be \"{sys.argv[0]} V MOD\"." )

	print( "Число, делитель:" )
	v = int(input( "v = " ))
	mod = int(input( "mod = " ))

#(v, mod) = (24791, 101)
#(v, mod) = (6303673663, 101)

# An integer length:
def dlen( x ):
	return len( str( x ) )


print( f"\nn = {v}, d = {mod}." )
vlen = dlen( v )
modlen = dlen( mod )
r = list()

for i in range( vlen ):
	powerten = ( 10 ** i )
	r.append( powerten % mod )
	print( f"r[{i}] = {powerten} % {mod} = {r[i]}" )


cur = v
prev = cur + 1
print()

# Same as "str[ pos ] = c"
def strindexrepl( s: str, pos: int, c: str ):
	return s[ : pos] + c + s[pos + 1 : ]

while dlen( cur ) != modlen  and  cur < prev:
	s = list( str( cur ) )
	curslen = len( s )
	vnew = 0

	print( f"r = ", end="" )

	output = str()

	for i in range( len( s ) ):
		ri = r[curslen - i - 1]
		vnew += ri * int(s[i])
		output += f"{ri}*{s[i]} + "

	output = strindexrepl( output, -2, '=' ) + str( vnew )
	prev = cur
	cur = vnew
	print( output )

if ( prev < cur ):
	print( f"  Следующий шаг {cur} ≥ предыдущего {prev}." )
else:
	print( f"  len(cur) == len(mod) == {modlen}, на следующих шагах ничего не изменится.", end="\n\n" )

if ( v == cur ):
	print( f"{v} не делится на {mod}." )
else:
	for i in range( mod, cur + mod, mod ):
		print( f" Сравнение {i} == {cur}" )

		if ( i >= cur ):
			break

	print( f"\nОтвет: {v}/{mod} ⇔ {cur}/{mod} " + ("(не " if cur % mod != 0 else "(" ) + "делится)." )
