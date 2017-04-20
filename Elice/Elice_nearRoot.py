def find_min_square_root(n):
    minimum = 0
    maximum = n
    sqrt_max = maximum ** (1.0 / 2.0)

    while (True):
        middle = int((maximum + minimum) / 2)

        if (middle ** 2 >= n):
            p = middle - 1
            if (p < sqrt_max and middle >= sqrt_max):
                return middle
            maximum = middle

        else:
            minimum = middle

def main():
    '''
    Do not change this code
    '''
    # n = int(input())
    n = 11298419211
    n = 112984192
    n = 1100
    n = 100
    q = find_min_square_root(n)
    print(q)

if __name__ == "__main__":
    main()
