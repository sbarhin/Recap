a = input()
b = input()
c = "".join(a.split())
d = "".join(b.split())
f = []
t = []
if len(c) != len(d):
    print("Not anagram")
else:
    for i in range(len(c)-1):
        if c[i] not in d:
            print("Not Anagram")
            break
        else:
            for j in c:
                if j in d:
                    f.append(j)
                else:
                    t.append(j)

    if (len(t) <= 0) | (len(f) <= 0):
        print("Anagram")


