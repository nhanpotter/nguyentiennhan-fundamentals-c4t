class rectangle:
    def __init__(self,w,l):
        self.w=w
        self.l=l
    def area(self):
        return self.w*self.l
a= float(input("Width? "))
b= float(input("Length?"))
print(rectangle(a,b).area())