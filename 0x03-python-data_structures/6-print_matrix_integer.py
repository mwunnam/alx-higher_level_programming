#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    rows = len(matrix)
    for x in range(rows):
        columns = len(matrix[x])
        for j in range(columns):
            print("{:d}".format(matrix[x][j]),
                  end=" " if j < columns - 1 else "")
        print()
