# Multiply elements of m1 and m2 to compute rows (start, end) of product
def mult_rows(m1, m2, start, end, result):
    for i in range(start, end):
        for j in range(DIM):
            for index in range(DIM):
                flat_index = i * DIM + j
                result[flat_index] += m1[i][index] * m2[index][j]
