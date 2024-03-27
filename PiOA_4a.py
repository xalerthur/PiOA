import sys

print( "Вычисление определителя матрицы методом Доджсона (Льюис Кэрролл)" )

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


# calculate determinant by Dodgson method
def calculate(matrix):

    step = 0
    matrix_size = len(matrix)

    # inner matrix for first step
    inner_matrix = [[1 for j in range(matrix_size-1)] for i in range(matrix_size-1)]

    # while matrix size is greater than 1
    while (matrix_size > 1):

        step += 1

        new_matrix = [[1 for j in range(matrix_size-1)] for i in range(matrix_size-1)]

        # one step of Dodgson method
        for i in range(matrix_size-1):
            for j in range(matrix_size-1):
                # если тут будет деление на 0, то иди нахуй
                new_matrix[i][j] = (matrix[i][j]*matrix[i+1][j+1] - matrix[i+1][j]*matrix[i][j+1])/inner_matrix[i][j]

        # print new matrix
        print_matrix(new_matrix, step)

        # update inner matrix
        inner_matrix = [[1 for j in range(matrix_size-2)] for i in range(matrix_size-2)]

        for i in range(1, matrix_size - 1):
            for j in range(1, matrix_size - 1):
                inner_matrix[i-1][j-1] = matrix[i][j]

        # update matrix
        matrix = new_matrix
        matrix_size -= 1

    return matrix[0][0]

def print_matrix(matrix, step=0):
    print(f'\nМатрица для шага {step}: ')
    for row in matrix:
        print(row)

# input_string = "1 0 -2 3 2; -1 -3 2 -2 0; -3 -2 2 -1 1; -2 3 -1 2 0; 0 -3 1 -1 -3"

input_string = input("\nВведите матрицу через пробелы и точку с запятой между строками: \n>")
matrix = parse_input(input_string)
check_matrix(matrix)
print_matrix(matrix)
print("\nОпределитель матрицы: ", calculate(matrix))