import sys

print( "Рачинский-Ⅲ" )

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

b = p % 10

print( f"\nn = {n}, p = {p}." )
print( f"Разбиваем делитель: a = {str(p)[: -1]}, b = {b}." )

if ( b in [3, 7] ):
	bstar = b
	print( f"  b ∈ {3, 7}  ⇒  b⁺ = b = {bstar}" )
else:
	bstar = 10 - b
	print( f"  b ∈ {1, 9}  ⇒  b⁺ = 10 - b = {bstar}" )

q = (p * bstar + 1)/10

if ( q - int(q) != 0.0 ):
	print( f"  q = (p * b⁺ + 1)/10 = ({p}*{bstar} + 1)/10 = {q}\n" )
	print( "Число q (", q, ") дробное!!!", sep="" )
	exit( 1 )

q = int(q)
print( f"  q = (p * b⁺ + 1)/10 = ({p}*{bstar} + 1)/10 = {q}" )

qstar = abs( p - q )
print( f"  q⁺ = abs(p - q) = abs({p} - {q}) = {qstar}\n" )


# Main cycle:
prev = n + 1
cur = n
stepnum = 1

while ( prev > cur  and  cur > p ):
	m = cur // 10
	k = cur % 10

	prev = cur
	cur = m - k * qstar

	print( f"{stepnum}) m = {m}, k = {k}" )

	if ( cur < 0 ):
		cur = -cur
		print( "   Берётся модуль числа:" )

	print( f"   m + kq⁺ = {cur}" )
	stepnum += 1

if ( cur <= p ):
	print( "Следующий шаг меньше делителя." )
else:
	print( "Цикл, следующий шаг больше или равен предыдущему." )


print( f"\nОтвет: {n}/{p}", "(не делится)." if ( n % p != 0 ) else "(делится)." )
