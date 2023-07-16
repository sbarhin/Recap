nums = {1,2,3,4,5,6}
nums = {0,1,2,3} & nums
print(nums)
nums = filter(lambda x: x > 1, nums)
print(len(list(nums)))

a = (lambda x: x*(x+1))(6)
print(a)

nums = [1, 2, 8, 3, 7]
print(list(filter(lambda x: x%2 ==0, nums)))


def func(**kwargs):
    print(kwargs["zero"])


func(a=0, zero=8)
