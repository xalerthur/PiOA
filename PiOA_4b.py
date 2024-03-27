import sys

print( "Вычисление определителя матрицы методом конденсации Чио при k = 1" )

# parse input string to matrix
def parse_input(input_string):
    
    # split string by semicolon
    rows = input_string.split(';')

    # rows to matrix
    matrix = []
    for row in rows:
        matrix.append(list(map(int, row.split())))

    return matrix

def check_matrix(matrix):

    # if matrix is empty
    if not matrix:
        print("Матрица пуста")
        sys.exit()
    
    # check if rows have equal length
    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            print("Строки матрицы имеют разную длину")
            sys.exit()
    
    # check if matrix is square
    if row_len != len(matrix):
        print("Матрица не квадратная")
        sys.exit()


# calculate determinant by Chio method
def calculate(matrix):
    
    step = 0
    factor = 1

    while len(matrix) > 1:

        step += 1

        matrix_size = len(matrix)
        new_matrix = [[0 for j in range(matrix_size-1)] for i in range(matrix_size-1)]

        # find good minor
        # find indexes of minimal element in matrix
        min_val = int(1e9)
        minor_i = 0
        minor_j = 0

        for i in range(matrix_size):
            for j in range(matrix_size):
                if abs(matrix[i][j]) < abs(min_val) and matrix[i][j] != 0:
                    min_val = matrix[i][j]
                    minor_i = i
                    minor_j = j

        # calculate new matrix
        count_i = 0
        count_j = 0

        for i in range(matrix_size):
            if i == minor_i:
                continue
            for j in range(matrix_size):
                if j == minor_j:
                    continue
                new_matrix[count_i][count_j] =  matrix[max(i, minor_i)][max(j, minor_j)] * matrix[min(i, minor_i)][min(j, minor_j)] - matrix[min(i, minor_i)][max(j, minor_j)] * matrix[max(i, minor_i)][min(j, minor_j)]
                count_j += 1
            count_i += 1
            count_j = 0

        print_matrix(new_matrix, factor, step)

        matrix = new_matrix
        factor *= min_val**(matrix_size-2)

    return (1/factor)*matrix[0][0]

def print_matrix(matrix, factor=1, step=0):
    print(f'\nМатрица для шага {step}: ')
    print(f'1/{factor}*')
    for row in matrix:
        print(row)

# input_string = "2 0 3 -2 3; 0 2 1 0 -2; 1 2 0 2 -2; -2 0 -3 0 3; -3 -3 2 3 2"

input_string = input("\nВведите матрицу через пробелы и точку с запятой между строками: \n>")
matrix = parse_input(input_string)
check_matrix(matrix)
print_matrix(matrix)
print("\nОпределитель матрицы: ", calculate(matrix))