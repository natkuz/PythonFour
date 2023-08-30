# Напишите функцию для транспонирования матрицы

def transpon_matrix(matrix: list):
    matrix_for_transpon = list(zip(*matrix))
    matrix_transpon = [list(i) for i in matrix_for_transpon]
    return matrix_transpon


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

print(transpon_matrix(matrix))