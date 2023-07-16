#Num = input("Enter a Number: ")
#Num = int(Num)
#print ( Num * 3 )

print("python" > "Python")

x = [6,4,2,9]
x = x[::-1]
print(x)
print(x[0]+x[2])

print("{0}{1}{0}".format("abra","cad"))

print("{c},{b},{a}".format(a=5,b=9,c=7))

print(max("hello"))

def amm(x):
    for i in range(x):
        print(i)
        return

amm(10)

def yes():
    word =""
    for ch in "spam":
        word += ch
        yield word

print(list(yes()))