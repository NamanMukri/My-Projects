class Circle():
    def __init__(self, r):
      self.r=r
    
    def __eq__(self, other):
      if (self.r==other.r):
        return True
      else:
        return False


if __name__ == '__main__':
    a=int(input("Enter Radius of circle 1:"))
    b=int(input("Enter Radius of circle 2:"))
    obj1=Circle(a)
    obj2=Circle(b)
    if (obj1==obj2):
      print("Output: True")
    else:
      print("Output: False")
    