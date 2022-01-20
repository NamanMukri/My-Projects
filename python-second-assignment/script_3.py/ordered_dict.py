from collections import OrderedDict
def order_dict(elements):
  elements = OrderedDict(elements)
  print(elements)

if __name__ == '__main__':
    count_of_elements = int(input("Enter no of Elements:"))
    elements ={}
    for i in range(1,count_of_elements+1):
        temp_variable = int(input("Input "+str(i)+":"))
        if temp_variable % 2 == 0:
          elements[temp_variable]=1
        else:
          elements[temp_variable]=0

    print(f"Dictionary: {elements}")
    order_dict(elements)
    
