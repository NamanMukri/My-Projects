def set_comprehension(input_object):
    
    set_using_comp = {int(i)*2 for i in input_object}
    
    return set_using_comp

if __name__ == '__main__':
    a=input("Add set elements seperated by space: ").split(' ')
    output = set_comprehension(a)
    print("Output Set using set comprehensions:", 
                                output)