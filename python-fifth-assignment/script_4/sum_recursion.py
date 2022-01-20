def recursive_list_sum(data_list):
    total = 0
    for element in data_list:
        if type(element) == type([]):
            total = total + recursive_list_sum(element)
        else:
            total = total + element

    return total


if __name__ == '__main__':
    a = input("Add list elements seperated by space ").split(' ')
    a = [int(x) for x in a]

    print(recursive_list_sum(a))