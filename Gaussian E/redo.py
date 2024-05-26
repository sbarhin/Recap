new_max = []


def calc(matrix, i=1, k=0):
    row = len(matrix)
    column = len(matrix[0])
    global new_max
    new_max.append(matrix[0])
    for _ in range(row - 1):
        new_max_1 = []
        for j in range(column):
            res = matrix[i][j] - ((matrix[i][k] / matrix[k][k]) * matrix[k][j])
            new_max_1.append(res)
        new_max.append(new_max_1)
        i += 1
    k += 1
    matrix[k::] = new_max[k+1::]
    return new_max


data = [[2, 0, 2, 8, 3], [3, 1, 4, 11, 9], [2, 4, 1, 6, 8],[4, 6, 5, 3, 5]]
result = calc(data)
print(result)
n = 0
size = len(data)
while n < size:
    if n != 0:
        calc(data,n,n)
    else:
        calc(new_max, n, n )
