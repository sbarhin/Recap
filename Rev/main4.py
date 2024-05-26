class A:
    def method(self):
        print(1)



class B(A):
    def method(self):
        print(2)
        super().method()


B().method()