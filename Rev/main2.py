def my_min(x, y, *args):
    if x < y:
        min_arg = min(list(args))
        if x < min_arg:
            return x
        elif x == min_arg:
            return x
        else:
            return min_arg

    elif y < x:
        min_arg = min(list(args))
        if y < min_arg:
            return y
        elif y == min_arg:
            return y
        else:
            return min_arg


def my_min1(x, y, *args):
    a = [x, y]
    a.extend(list(args))
    return min(a)


print(my_min(8, 13, 4, 42, 120, 7))
print(my_min1(8, 13, 4, 42, 120, 7))
