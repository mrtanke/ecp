def func(number_sequence, start, end, result):
    for i in range(start, end):
        result[i] = pow(number_sequence[i], 3)