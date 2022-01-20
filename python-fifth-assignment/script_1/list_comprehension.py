def list_comprehension(input_object):
    list_using_comp = [int(i)*2 for i in input_object]
    return list_using_comp
    

if __name__ == '__main__':
    a = (input("Add list elements seperated by space: ").split(' '))
    output = list_comprehension(a)
    print("Output list using list comprehensions:",
          output)