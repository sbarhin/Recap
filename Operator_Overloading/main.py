class Shape:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    @property
    def area(self):
        return self.width * self.height

    def __add__(self, o):
        return Shape(self.width + o.width, self.height + o.height)

    def __gt__(self, o):
        # return self.width * self.height > o.width * o.height
        return self.area > o.area


w1 = int(input())
w2 = int(input())
h1 = int(input())
h2 = int(input())

s1 = Shape(w1, h1)
s2 = Shape(w2, h2)
result = s1 + s2
print(result.area)
print(s1 > s2)

