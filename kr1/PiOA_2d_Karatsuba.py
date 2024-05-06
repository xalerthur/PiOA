import sys

print('karatsuba')
if len( sys.argv ) == 3:
	a = int(sys.argv[1])
	b = int(sys.argv[2])
	print(f'a = {a}\nb = {b}\n')
else:
	if len( sys.argv ) != 1:
		print( "Incorrect arguments usage, should be \"{sys.argv[0]} A B\"." )

	a = int(input( "a = " ))
	b = int(input( "b = " ))

def round_up(n):
    if n & (n - 1) == 0:
        return n
    else:
        return 2 ** (len(bin(n)) - 2)



def to_arr(n):
    return [int(d) for d in str(n)]

# a = 331
# b = 22

ar = to_arr(a)
br = to_arr(b)

mul_count = 0

if len(ar) < len(br):
    a, b = b, a
    ar, br = br, ar

ar = [0] * (round_up(len(ar)) - len(ar)) + ar
br = [0] * (len(ar) - len(br)) + br


def karatsuba(a: int, b: int):
    if a < 10 and b < 10:
        if not(a in [0, 1] or b in [0, 1]):
            global mul_count
            mul_count += 1
        # print(f'{a} * {b} = {a * b}')
        return a * b
    else:
        n = round_up(max(len(str(a)),len(str(b)))) // 2
        a1 = a // 10**n
        a2 = a % 10**n
        b1 = b // 10**n
        b2 = b % 10**n

    p1 = karatsuba(a1, b1) # higher coeffs
    p2 = karatsuba(a2, b2) # lower coeffs
    t = karatsuba(a1 + a2, b1 + b2)
    print('-' * 20)
    print(f'a = {a}')
    print(f'b = {b}')
    print(f'p1 = {a1} * {b1} = {p1}')
    print(f'p2 = {a2} * {b2} = {p2}')
    print(f't = {a1 + a2} * {b1 + b2} = {t}')
    print(f'{a} * {b} = {p1} * 10^{2 * n} + ({t} - {p1} - {p2}) * 10^{n} + {p2}')
    print('-' * 20)
    return p1 * 10 ** (2 * n) + (t - p1 - p2) * 10 ** n + p2

print(f'karatsuba: {karatsuba(a,b)}')
print(f'check a*b: {a * b}')
print(f'{mul_count = }')