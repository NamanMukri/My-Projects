
from collections import defaultdict
def default_dict(elements):
  default_list=defaultdict(int)
  length=len(elements)
  for i in range(1,(length+1)):
    default_list[i] = elements[i-1]
  print("OrderedDict: ",default_list)
if __name__ == '__main__':
    count_of_elements = int(input("Enter no of Elements:"))
    elements = []
    for i in range(1,count_of_elements+1):
      temp_variable = int(input("Input "+str(i)+":"))
      elements.append(temp_variable)
    print("List: ",elements)
    default_dict(elements)
   
    
    
