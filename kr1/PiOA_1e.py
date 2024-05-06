import sys

if len(sys.argv) == 3:
    n = int(sys.argv[1])
    d = int(sys.argv[2])
    print(f'n = {n}\nd = {d}\n')
else: 
    n = int(input("n = "))
    d = int(input("d = "))


def find_min_decomposition(n, d):
    min_i = 0
    min_dec = n
    for i in range(1, len(str(n))):
        s = 10 ** i
        a = n // s
        b = n % s
        rs = s % d

        dec = a * rs + b
        if dec < min_dec:
            min_dec = dec
            min_i = i

        # print(f"{a} * {rs} + {b} = {dec}")

    return min_i, min_dec

cur_n = n
it = 1
while len(str(cur_n)) > len(str(d)):
    old_n = cur_n
    m_i, cur_n = find_min_decomposition(cur_n, d)
    s = 10 ** m_i
    rs = s % d
    a = old_n // s
    b = old_n % s
    print(f'{it}) a = {a}, b = {b}, r_{m_i} = 10**{m_i} % {d} = {rs}')
    print(f'   r_{m_i} * a + b = {rs} * {a} + {b} = {cur_n}\n')
    it += 1

print(f'{n}/{d} ⇔ {cur_n}/{d}')
print(f'{n} делится на {d}' if cur_n % d == 0 else f'{n} не делится на {d}')
print(f'{n} / {d} = {n / d}')
