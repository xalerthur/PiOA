import numpy as np

matA = np.matrix( [
	[1, 1, 1, 1],
	[2, 2, 2, 2],
	[3, 3, 3, 3],
	[4, 4, 4, 4]
] )
matB = np.matrix( [
	[1, 2, 3, 4],
	[8, 7, 6, 5],
	[9, 0, 1, 2],
	[9, 9, 4, 3]
] )


def split(matrix: np.matrix):
	"""
	Splits a given matrix into quarters.
	Input: nxn matrix
	Output: tuple containing 4 n/2 x n/2 (matrix) corresponding to a, b, c, d
	"""
	row, col = matrix.shape
	row2, col2 = row//2, col//2
	return matrix[:row2, :col2], matrix[:row2, col2:], matrix[row2:, :col2], matrix[row2:, col2:]


def colstrlens(matrix) -> list:
	"""
	Gets a len(str(longest_int)) for each column. Not used right now, but can be implemented to enhance readability.
	Input: matrix n*n
	Output: list of length n containing minimal char length in every column for pretty output
	"""
	mt = matrix.transpose().tolist()

	# Lambda selects longest string representation from the column:
	colstrlen = lambda col: max( len(str(x)) for x in col )

	# List of longest values in every column:
	return [ colstrlen( col ) for col in mt ]


def __indent( depth: int ) -> str:
	return ('    ' * depth)

def npmatrixp( mdata ) -> str:
	return (mdata.tolist() if len(mdata) > 1 else mdata[0, 0])

def __printstrassen( text, mdata, depth: int = 0 ) -> str:
	# return
	if type(mdata) == np.matrix:
		arg3 = npmatrixp( mdata )
	elif type(mdata) == list and len(mdata) > 1:
		arg3 = mdata[0]
	elif mdata is None:
		arg3 = ''
	else:
		arg3 = mdata

	print( __indent( depth ), text, arg3, sep='' )

'''
def __strassen_nextp( pnum: int, e1str: str, e2str: str, depth: int ) -> int:
	if len(e1str) > 1: e1str = '(' + e1str + ')'
	if len(e2str) > 1: e2str = '(' + e2str + ')'

	printstrassen( f"Смотрим P{pnum} = {e1str.upper()} * {e2str.upper()}: " )
	e1 = exec(e1str)
	e2 = exec(e2str)
	p = strassen(exec(e1), exec(e2), depth + 1)

	e1calc = re.sub( "", "", e1str )
	printstrassen( f"P{pnum} = {npmatrixp(a)} * ({npmatrixp(f)} - {npmatrixp(h)}) = ", p1, +1 )
	return p
# '''



globalmatrixstep = 0


def strassen(x: np.matrix, y: np.matrix, depth: int = 0):
	"""
	Computes matrix product by divide and conquer approach, recursively.
	Input: matrix X n*n, matrix Y n*n
	Output: nxn matrix, product of x and y
	"""

	indent = lambda ofs=0 : __indent( depth + ofs )
	printstrassen = lambda text, mdata=None, depthofs=0 : __printstrassen( text, mdata, depth + depthofs )

	# Base case when shape is 1x1
	if len(x) == 1:
		return x * y

	global globalmatrixstep
	globalmatrixstep += 1
	curmatrixstep = globalmatrixstep
	printstrassen( ">>>>> НАЧАЛО УМНОЖЕНИЯ ШТРАССЕНА #", curmatrixstep )


	# Splitting input into quadrants. This will be done recursively
	# until the base case is reached.
	printstrassen( "Матрица 1: ", x )
	#print( indent(), "Матрица 1: ", x.tolist(), sep='' )
	a, b, c, d = split(x)
	printstrassen( 'A = (м1↖) = ', a, +1 )
	printstrassen( 'B = (м1↗) = ', b, +1 )
	printstrassen( 'C = (м1↙) = ', c, +1 )
	printstrassen( 'D = (м1↘) = ', d, +1 )
	#print( indent(+1), 'A = (м1↖) = ', a.tolist(), sep='' )
	#print( indent(+1), 'B = (м1↗) = ', b.tolist(), sep='' )
	#print( indent(+1), 'C = (м1↙) = ', c.tolist(), sep='' )
	#print( indent(+1), 'D = (м1↘) = ', d.tolist(), sep='' )

	printstrassen( "Матрица 2: ", y )
	e, f, g, h = split(y)
	printstrassen( 'E = (м2↖) = ', e, +1 )
	printstrassen( 'F = (м2↗) = ', f, +1 )
	printstrassen( 'G = (м2↙) = ', g, +1 )
	printstrassen( 'H = (м2↘) = ', h, +1 )

	# Computing the 7 products, recursively (p1, p2...p7)
	printstrassen( "Смотрим P1 = A * (F-H): " )
	printstrassen( "Результат (F-H) = ", f - h, +1 )
	p1 = strassen(a, f - h, depth + 1)
	printstrassen( f"Итого P1 = {npmatrixp(a)} * ({npmatrixp(f)} - {npmatrixp(h)}) = ", p1, +1 )

	printstrassen( "Смотрим P2 = (A+B) * H:" )
	printstrassen( "Результат (A+B) = ", a + b, +1 )
	p2 = strassen(a + b, h, depth + 1)
	printstrassen( f"Итого P2 = ({npmatrixp(a)} + {npmatrixp(b)}) * {npmatrixp(h)} = ", p2, +1 )

	printstrassen( "Смотрим P3 = (C+D) * E:" )
	printstrassen( "Результат (C+D) = ", c + d, +1 )
	p3 = strassen(c + d, e, depth + 1)
	printstrassen( f"Итого P3 = ({npmatrixp(c)} + {npmatrixp(d)}) * {npmatrixp(e)} = ", p3, +1 )

	printstrassen( "Смотрим P4 = D * (G-E): " )
	printstrassen( "Результат (G-E) = ", g - e, +1 )
	p4 = strassen(d, g - e, depth + 1)
	printstrassen( f"Итого P4 = {npmatrixp(d)} * ({npmatrixp(g)} - {npmatrixp(e)}) = ", p4, +1 )

	printstrassen( "Смотрим P5 = (A+D) * (E+H): " )
	printstrassen( "Результат (A+D) = ", a + b, +1 )
	printstrassen( "Результат (E+H) = ", e + h, +1 )
	p5 = strassen(a + d, e + h, depth + 1)
	printstrassen( f"Итого P5 = ({npmatrixp(a)} + {npmatrixp(d)}) * ({npmatrixp(e)} - {npmatrixp(h)}) = ", p5, +1 )

	printstrassen( "Смотрим P6 = (B-D) * (G+H): " )
	printstrassen( "Результат (B-D) = ", b - d, +1 )
	printstrassen( "Результат (G+H) = ", g + h, +1 )
	p6 = strassen(b - d, g + h, depth + 1)
	printstrassen( f"Итого P6 = ({npmatrixp(b)} - {npmatrixp(d)}) * ({npmatrixp(g)} - {npmatrixp(h)}) = ", p6, +1 )

	printstrassen( "Смотрим P7 = (A-C) * (E+F): " )
	printstrassen( "Результат (A-C) = ", a - c, +1 )
	printstrassen( "Результат (E+F) = ", e + f, +1 )
	p7 = strassen(a - c, e + f, depth + 1)
	printstrassen( f"Итого P7 = ({npmatrixp(a)} - {npmatrixp(c)}) * ({npmatrixp(e)} - {npmatrixp(f)}) = ", p7, +1 )


	# Computing the values of the 4 quadrants of the final matrix c
	c11 = p5 + p4 - p2 + p6
	print( indent(), "C11 = p5 + p4 - p2 + p6 = ", npmatrixp( c11 ), sep='' )
	c12 = p1 + p2
	print( indent(), "C12 = p1 + p2           = ", npmatrixp( c12 ), sep='' )
	c21 = p3 + p4
	print( indent(), "C21 = p3 + p4           = ", npmatrixp( c21 ), sep='' )
	c22 = p1 + p5 - p3 - p7
	print( indent(), "C22 = p1 + p5 - p3 - p7 = ", npmatrixp( c22 ), sep='' )

	#print( indent, printc11, printc12, '\n', printc21, printc22, f'  maxlen {colstrlens(c11)}', sep='', end='\n\n' )

	c = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))
	printstrassen( "<<<<< КОНЕЦ УМНОЖЕНИЯ ШТРАССЕНА #", curmatrixstep )
	#printstrassen( f'Max col len for {c.tolist()} is {colstrlens(c)}' )
	depth -= 1

	print()
	if curmatrixstep == 1:
		globalmatrixstep = 0
	return c

def main():

	print( "Результат перемножения:\n", strassen( matA, matB ) )
	print(matA * matB)
	print('\n(Умножаемые матрицы задаются через изменение "matA" и "matB" в начале файла исходного кода!)')

if __name__ == '__main__':
	main()