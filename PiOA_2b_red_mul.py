import sys

def to_arr(n):
    return [int(d) for d in str(n)]

print("Сокращенное умножение")

if len( sys.argv ) == 3:
	a = int(sys.argv[1])
	b = int(sys.argv[2])
	print(f'a = {a}\nb = {b}\n')
else:
	if len( sys.argv ) != 1:
		print( "Incorrect arguments usage, should be \"{sys.argv[0]} A B\"." )

	a = int(input( "a = " ))
	b = int(input( "b = " ))

# a = 251568
# b = 32571


ar = to_arr(a)
br = to_arr(b)

if len(ar) < len(br):
    a, b = b, a
    ar, br = br, ar

br = [0] * (len(ar) - len(br)) + br

levels = []
lev_str = []
for step in range(len(br)):
    levels.append([])
    if step == 0:
        for sa, sb in zip(ar, br):
            levels[-1].append(sa * sb)
        lev_str.append(''.join(map(lambda x: f'{x:0>2}', levels[-1])))
    else:
        add = 0
        for shifted_idx in range(len(br) - step):
            levels[-1].append(ar[shifted_idx] * br[shifted_idx + step] \
                + ar[shifted_idx + step] * br[shifted_idx])
            if shifted_idx != 0:
                add = levels[-1][-1] // 100
                levels[-1][-1] %= 100

                levels[-1][shifted_idx - 1] += add
        lev_str.append(''.join(map(lambda x: f'{x:0>2}', levels[-1]))+'0'*step)

res = sum(map(int, lev_str))

max_len = max(map(len, lev_str))
# align in center

print(f'{a:>{max_len}}')
print(f'{b:>{max_len}}')
print('-' * max_len)
for idx, s in enumerate(lev_str):
    cur_s = f'{s:>{max_len}}'[:-idx if idx else max_len].ljust(max_len, ' ')      
    print(cur_s)
print('-' * max_len)
print(f'{res:>{max_len}}')

print(f'{a * b = }')