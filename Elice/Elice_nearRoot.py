def find_min_square_root(n):
    l = [i for i in range (1, n + 1)]

    length = len(l)
    minimum = l[0]
    maximum = l[length - 1]
    sqrt_max = maximum ** (1.0 / 2.0)

      while (True):
        middle = int((maximum + minimum) / 2)
        if (l[middle] == maximum):
            middle -= 1
        elif (l[middle] == minimum):
            middle += 1
        q = l[middle]

        if (q ** 2 >= n):
            print("1 : " + str(minimum) + " : " + str(q) + " : " + str(maximum))
            p = q - 1
            if (p < sqrt_max and q >= sqrt_max):
                return q
            maximum = q

        else:
            print("2 : " + str(minimum) + " : " + str(q) + " : " + str(maximum))
            minimum = q
    
def main():
    '''
    Do not change this code
    '''
    n = int(input())
    q = find_min_square_root(n)
    print(q)

if __name__ == "__main__":
    main()
