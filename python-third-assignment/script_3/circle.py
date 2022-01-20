class Circle():
    def __init__(self, r):
        self.r = r

    def area(self):
        area = 3.14 * self.r * self.r
        return area

    def circumference(self):
        circum = 3.14*2*self.r
        return circum

    def __eq__(self, other):
        if (self.r == other.r):
            return True
        else:
            return False

    def __add__(self, other):
        return ""

    def __gt__(self, other):
        if (self.r > other.r):
            return True
        else:
            return False


if __name__ == '__main__':
    a = int(input("Enter Radius of circle 1:"))
    b = int(input("Enter Radius of circle 2:"))
    obj1 = Circle(a)
    obj2 = Circle(b)
    print("Circumference of circle 1: {}".format(obj1.circumference()))
    print("Circumference of circle 2: {}".format(obj2.circumference()))
    print("Area of circle 1: {}".format(obj1.area()))
    print("Area of circle 2: {}".format(obj2.area()))
    if obj1 == obj2:
        print("Both Circles are Equal")
    elif obj1 > obj2:
        print("Circle 1 is bigger than Circle 2")
    else:
        print("Circle 2 is bigger than Circle 1")
