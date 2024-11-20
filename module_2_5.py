from random import vonmisesvariate


def get_matrix(n, m, value):
    if n <= 0 or m <= 0:
        return []

    matrix = []

    for _ in range(n):
        list = []

        for _ in range(m):
            list.append(value)

        matrix.append(list)
    return matrix

result1 = get_matrix(2, 2, 'pop')
result2 = get_matrix(2, 3, 'corn')
result3 = get_matrix(4, 1, 'juice')
print(result1)
print(result2)
print(result3)