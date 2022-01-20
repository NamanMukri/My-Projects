def power(N,P):
    if P > 1:
        return (N * power(N,(P-1)))
    else:
        return (N)


# Driver program
if __name__ == '__main__':
    a = int(input("Enter the number "))
    b = int(input("Enter Power "))

    print(power(a, b))