def column(matric, col=0, row=0):
    res = []
    for i in range(row, len(matric)):
        res.append(matric[i][col])
    return res


# my phone is running low so text anything here
new_max = []  # making new_max a global variable


# R2 * R3 -R3 ---> r3???yhh ok
# the R2 IS FROM NEW_MAX AND R3 IS FROM INCOMING MATRIX RIGHT?
#  yhh
# is there a copy of what i did? they're commented some are deleted
# no.. it was the chat i delted
# so in r3 it will be
# [0, 0, 0, 40, 120]?? which side..R3 after yesok
# ei wait o... i don't know why it's making it generator obj let yield it err
# in fact, the i and j serves the same purpose
# it's incomplete the code?
# it wasn't in the first code

def calc(matrix, i=0, j=0):  # row and columnwhat's the j for? took care of the first cal
    # calculation for all items in the matrix
    global new_max
    print(f'incoming matrix {matrix}')
    r = len(matrix)
    l = len(matrix[0])
    if i:
        new_max = matrix[:i:]
    print(f'new max before operation: {new_max=}')
    # WHEN FIRST ROW FIRST COLUMN IS 1...HOLD ON
    # so when i=1, it'll start on second row yh
    if matrix[i][i] == 1:
        new_max.append(matrix[i])
        # for _ in matrix[i + 1::]:
        for x in range(i, r-1):
            zipped = zip(new_max[x], matrix[x + 1])
            # should it always be a*b - b? shouldn't t be a scalar multiple? i chose
            #that cause of the path i decided on..it was going to work for all..
            #after including the swapping and tetc
            # me kraa mabr3 i'm gonig to bat hand pray and eat,
            # eat bath and pray hahhha....i wanted to have a copy of the inital...
            #so i can continue from there...rmeove my code then...no be small work oo
            #how to merge them back? you'll merge sth?
            # the mains i don't get you o
            # just remove mine or i should do for you?
            # THE where i have highlighed . There are two mains
            # ahn oh, it's the same thing, close one..byeeeeepkok jazakallahyou too
            new_max.append([a * b - b for a, b in zipped])

            # new_max_1 = []
            # sign = column(matrix, i + 1)[j + 1] // column(matrix, i + 1)[j + 1]
            # # print(column(matrix)[j + 1])
            # amend = new_max[i][i] * column(matrix, i + 1)[j + 1] - (sign * column(matrix, i + 1)[j + 1])
            # new_max_1.append(amend)
            # for stuff in range(l - 1):
            #     sign = matrix[j + 1][i + 1] // matrix[j + 1][i + 1]
            #     new_mend = new_max[i][stuff + 1] * matrix[j + 1][i + 1] - (sign * matrix[j + 1][i + 1])
            #     new_max_1.append(new_mend)
            # new_max.append(new_max_1)
            # j += 1
    else: # if the first item in the row is 0, what happens? That's where we swap...
        #haven't done that
        # there's sth wrong... see this[[1, -2, 1, 0], [0, -3, 0, -5], [0, -3, 0, -5]]
        # it's not supposed to be so' the R3
        resolve = [0 if x == 0 else x / matrix[i][i] for x in matrix[i]]
        new_max.append(resolve)

        if column(matrix)[i + 1::] == 0:
            pass
        else:

            # for _ in matrix[i + 1::]:
            for x in range(i, r-1):
                zipped = zip(new_max[x], matrix[x + 1])
                new_max.append([a * b - b for a, b in zipped])

                # new_max_1 = []
                # try:
                #     sign = column(matrix, i + 1)[j + 1] // column(matrix, i + 1)[j + 1]
                # except:
                #     sign = 1
                # amend = new_max[i][i] * column(matrix, i + 1)[j + 1] - (sign * column(matrix, i + 1)[j + 1])
                # new_max_1.append(amend)
                #
                # for stuff in range(l - 1):
                #
                #     sign = matrix[j + 1][i + 1] // matrix[j + 1][i + 1]
                #     new_mend = new_max[i][stuff + 1] * matrix[j + 1][i + 1] - (sign * matrix[j + 1][i + 1])
                #     new_max_1.append(new_mend)
                # new_max.append(new_max_1)
                # j += 1
    i += 1
    matrix[i::] = new_max[i + 1::]  # what is it doing? seting 1 to 0
    print(f'new max after operation: {new_max=}')
    # return new_max


# iteration 0 has 4 columns, 1 has 3, 2 has 2....

# data = [[2, 4, 6, 8, 10], [4, 6, 8, 10, 12], [6, 8, 10, 12, 14], [8, 10, 12, 14, 16]]
data = [[1, -2, 1, 0], [2, 1, -3, 5], [4, -7, 1, -1]]
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
# new matrix
# instead of
# miscalculation, mm
# you should determine the operation sign.
# it might not always be minus ohk
# it's cos always before calculation, i make the dominant first row
# first column 1...


# apart from the sign
# see (0*40 -(40) = -40
# is it always using the 0 to determine?
# shouldn't it use the -40? to dm it will eventually multiply
# 0 * -84 --84 so determing the sign from the column element and make it mi
# show me where it is
