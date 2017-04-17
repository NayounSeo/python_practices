# 활동 선택 문제 - activity selection
def find_min_room(num_class, classes):
    if (num_class == 0):
        return 0

    min_rooms = 1
    classes = sorted (classes, key=lambda a: a[1])
    rooms = [classes[0]]
    del classes[0]

    for i in classes:
        rooms = sorted(rooms, key=lambda a: a[2])
        fastest = rooms[0]
        if (fastest[2] <= i[1]):
            ind = rooms.index(fastest)
            rooms[ind] = i
        else:
            rooms.append(i)
            min_rooms += 1

    return min_rooms, rooms


def read_inputs():
    num_class = int(input())
    classes = []
    for i in range(num_class):
        line = [int(x) for x in input().split()]
        class_no = line[0]
        start = line[1]
        end = line[2]
        classes.append((class_no, start, end))

    return num_class, classes

def main():
    # num_class, classes = read_inputs()
    num_class = 8
    classes = [(6, 15, 21), (7, 20, 25), (1, 3, 8), (3, 2, 14), (8, 6, 27), (2, 7, 13), (4, 12, 18), (5, 6, 20)]
    ans, r = find_min_room(num_class, classes)
    print(ans)



if __name__ == "__main__":
    main()

'''
입력 예시 
8  
6 15 21  
7 20 25  
1 3 8  
3 2 14  
8 6 27  
2 7 13  
4 12 18  
5 6 20
'''