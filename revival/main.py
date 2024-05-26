def subprod_sum(num: str):
    prod, sum_ = 1, 0
    for i in num:
        prod *= int(i)
        sum_ += int(i)
    return prod - sum_


a = subprod_sum("255")
print(a)


a = [2,3,1,4,5]
b = 4
c = []

for i in range(len(a)-1):
    for j in range(len(a)-(i+1)):
        d = a[i] + a[j+i+1]
        c.append(d)
        print(c)
        if a[i] + a[j+i+1] == b:
            print(i,i+j+1)
print(c)
'''class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(len(nums)-(i+1)):
                d = nums[i] + nums[j+i+1]
                if nums[i] + nums[j+i+1] == target:
                    return i,i+j+1'''


b = ["5","-2","4","C","D","9","+","+"]
c = []
for i in b:
    if i.lstrip("-+").isdigit():
        c.append(int(i))
        print(c)
    elif i == "C":
        if not c:
            c.append(0)
        else:
            c.remove(c[-1])
        print(c)
    elif i == "D":
        if not c:
            c.append(0)
        else:
            c.append(c[-1] * 2)
        print(c)
    elif i == "+":
        c.append(c[-1] + c[-2])
total = sum(c)
print(c)
print(total)

"""OR"""

ans = []

for i in b:
    if i == "+" and len(b) > 2:
        ans.append(ans[-2] + ans[-1])
    elif i == "D":
        ans.append(ans[-1] * 2)
    elif i == "C" and len(b) > 1:
        ans.pop()
    else:
        ans.append(int(i))

print(sum(ans))


logs = ["d1/", "d2/", "../", "d21/", "./"]
b = 0
for i in logs:
    if i == "../":
        if b != 0:
            b += 0
    elif i == "./":
        b -= 1
    else:
        b += 1

print(b)


a = bin(7).lstrip("0b")
for i in a:
    c = a.count("1")
print(c)


# d = [[1,1],[3,7],[2,12],[7,17]]
d = [[0,10],[1,20]]
result = []
comp = []
for i in range(len(d)):
    if i == 0:
        result.append(d[0][1])
    else:
        result.append(d[i][1]-d[i-1][1])

if result.count(max(result)) != 1:
    a = [comp.append(d[j][0]) for j in range(len(result)) if result[j] == max(result)]
    print(min(comp))
else:
    print(d[result.index(max(result))][0])


# g = "abbcccddddeeeeedcba"
g = "j"
new = []
a = 1
if len(g) == 1:
    new.append(a)
else:
    for i in range(len(g)-1):  # Iterate to calculate the maximum consecutive number
        if g[i] == g[i+1]:  # if letter is equal succeeding letter, add one to 'a'
            a += 1
        else:              # if not set 'a' to 1
            a = 1
        new.append(a)
print(max(new))


x = 512
y = x
result = ""
while x:
    if x < 0:                       # if x is a negative number,
        x = int(str(x).lstrip("-"))  # strip the negative sign in front of the number
    else:                           # calc for positive number
        result += str(x % 7)
        x = x//7
if y < 0:                            # adding the negative sign after calc and returning the reverse of the result
    result += "-"
    b = int(result[::-1])
    print(type(b))
else:                                  # returning the reverse of the positive decimal number
    b = int(result[::-1])
    print(type(b))



