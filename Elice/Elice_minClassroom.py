# 활동 선택 문제

def find_min_room(num_class, classes):
    # classes = [(no, start, end), ...]
    # 시작 시간에 맞게 정렬
    classes = sorted (classes, key=lambda a: a[2])

    # classes = sorted (classes, key=operator.itemgetter(0, 1))
    rooms = [classes[0]]
    min_rooms = 1
    del classes[0]
    
    earliest_bye = rooms[j][2]
    bye_ind = 0;
    for i in classes:
        for j in rooms: # 가장 빨리 끝나는 회의를 탐색
            # if (j[2] <= i[1]):
            if (j[2] < earliest_bye):
                earliest_bye = j[2];
                bye_ind = rooms.index(j)

        if (ealist_bye < i[1]):
            rooms[bye_ind] = i
        elif:
            rooms.append(i)
            min_rooms += 1
        rooms = sorted (rooms, key=lambda a: a[2]) # 끝나는 시간이 빠른 순서대로

    return min_rooms


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
    ans = find_min_room(num_class, classes)
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