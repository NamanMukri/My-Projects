if __name__== '__main__':
    dict1 = {"a": 25, "b": 4, "c": 1, "d": 100}
    dict1={k: dict1.get(k, 0) ** 0.5 for k in dict1.keys()}
    print(dict1)

