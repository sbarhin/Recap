class Shape:
    def __int__(self, width, height):
        self.width = width
        self.height = height

    @staticmethod
    def area(width, height):
        return width * height


w = int(input())
h = int(input())
print(Shape.area(w, h))


a = "1adwerr"
print(a[0])