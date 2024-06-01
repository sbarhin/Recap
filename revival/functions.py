# output the sound of an animal
def animal(name):
    sound = {"dog": "bark", "lion": "roar", "frog": "croak", "bee": "buzz", "cat": "purr"}
    if not sound:
        return sound.get(name)
    return None


a = animal("sheep")
print(a)


# checking the arrangement or oder of brackets
open_lst = ["[", "{", "("]
close_lst = ["]", "}", ")"]


def check_order(s):
    stack = []
    for i in s:
        if i in open_lst:
            stack.append(i)
        elif i in close_lst:
            pos = close_lst.index(i)
            if (len(stack) > 0) and (open_lst[pos] == stack[len(stack) - 1]):
                stack.pop()
            else:
                return "Unbalanced"
    if len(stack) == 0:
        return "Balanced"
    else:
        return "Unbalanced"


print(check_order("{[][]}"))
