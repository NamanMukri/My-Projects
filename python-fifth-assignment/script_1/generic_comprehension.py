def generic_comprehension(input_object):
    generic_using_comp = (int(i) * 2 for i in input_object)
    return generic_using_comp


if __name__ == '__main__':
    a = input("Add generic elements seperated by space: ").split(' ')
    output = generic_comprehension(a)
    print("Output generic list using generic comprehensions:",
          list(output))