def column(matric, col=0, row=0):
    res = []
    for i in range(row, len(matric)):
        res.append(matric[i][col])
    return res



new_max = []


def calc(matrix, i=0, j=0):
    global new_max
    print(f'incoming matrix {matrix}')
    r = len(matrix)
    l = len(matrix[0])
    if i:
        new_max = matrix[:i:]
    print(f'new max before operation: {new_max=}')
    if matrix[i][i] == 1:
        new_max.append(matrix[i])
        if i == 1:
             print(f'column(matrix): {column(matrix)}')
        for _ in matrix[i + 1::]:
            new_max_1 = []
             #sign = column(matrix, i + 1)[j + 1] // column(matrix, i + 1)[j + 1]
            # print(column(matrix)[j + 1])
            amend = new_max[i][i] * column(matrix)[j + 1] - column(matrix)[j + 1]
            new_max_1.append(amend)
            for stuff in range(l - 1):
                 #sign = matrix[j + 1][i + 1] // matrix[j + 1][i + 1]
                new_mend = new_max[i][stuff + 1] * matrix[j + 1][i + 1] - matrix[j + 1][i + 1]
                new_max_1.append(new_mend)
            new_max.append(new_max_1)
            j += 1
    else:
        resolve = [x / matrix[i][i] for x in matrix[i]]
        new_max.append(resolve)
        if column(matrix)[i + 1::] == 0:
            pass
        else:
            for _ in matrix[i + 1::]:

                new_max_1 = []
                try:
                     sign = column(matrix, i + 1)[j + 1] // column(matrix, i + 1)[j + 1]
                except:
                     sign = 1
                amend = new_max[i][i] * column(matrix)[j + 1] - (sign * column(matrix)[j + 1])
                new_max_1.append(amend)
                for stuff in range(l - 1):
                    sign = matrix[j + 1][i + 1] // matrix[j + 1][i + 1]
                    new_mend = new_max[i][stuff + 1] * matrix[j + 1][i + 1] - (sign * matrix[j + 1][i + 1])
                    new_max_1.append(new_mend)
                new_max.append(new_max_1)
                j += 1
    i += 1
    matrix[i::] = new_max[i + 1::]
    print(f'new max after operation: {new_max=}')
    # return new_max

data = [[1, 4, 6, 8, 10], [4, 6, 8, 10, 12], [6, 8, 10, 12, 14], [8, 10, 12, 14, 16]]
#data = [[1, -2, 1, 0], [2, 1, -3, 5], [4, -7, 1, -1]]
# calc(data)  # yh 4 rows 5 columns
# roww = int(input("The number of rows: "))
# colum = int(input("The number of column, the equal to inclusive: "))
# a = []
# print("Type the numbers in the column accordingly")
# for i in range(roww):
#     b = []
#     for j in range(colum):
#         f = int(input())
#         b.append(f)
#     a.append(b)
# print(a)
# while a
# calc(a,roww,column)
n = 0
size = len(data)
while n < size:
    # print(f'iteration {n=}')
    if not n:
        calc(data, n, n)
    else:
        calc(new_max, n, n)
    n += 1
print(new_max)
