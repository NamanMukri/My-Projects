class Rectangle():
    def __init__(self, l, w):
      self.l=l
      self.w=w


    def rectangle_area(self):
        area=self.l*self.w
        return "Area of rectangle:{}".format(area)


if __name__ == '__main__':
    a=int(input("Enter length of rectangle: "))
    b=int(input("Enter breadth of rectangle:  "))
    newRectangle = Rectangle(a, b)
    print(newRectangle.rectangle_area())