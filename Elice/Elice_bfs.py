## nodes: list of connected nodes of each node (인접 리스트)
## example: [[1,2],[0,2],[0,1]] for a cyclic graph with 3 nodes
## return: list of nodes in the shortest path
def simple_path(nodes):
    start = 0
    end = len(nodes) - 1
    
    # init
    vertex = []
    que = []
    for i in range(end + 1):
        # 정점 번호, 방문 여부 (w/g/b), 가까운 정점, 0으로부터의 거리
        vertex.append([i, 'w', 0, 0])
    vertex[0] = [0, 'g', 0, 0]
    que.append(vertex[0])
    
    # search
    # TODO : que를 que[i][0], que[i][3]에 따라 정렬하기!
    while (que != []):
        que = sorted(que, key=lambda x:(x[3], x[2]))
        v_s = que[0]
        v = v_s[0] # 정점 번호
        print (que)
        del que[0]

        for edge in nodes[v]:
            if (vertex[edge][1] == 'w'):
                vertex[edge][1] = 'g' # 탐색 중
                vertex[edge][2] = v
                vertex[edge][3] = vertex[v][3] + 1
                que.append(vertex[edge])
        vertex[v][1] = 'b' # 탐색 종료
    
    print (vertex)

    near_v = end
    result = []
    while (near_v != 0):
        result.append(near_v)
        near_v = vertex[near_v][2]
    result.append(0)
    result = sorted(result)

    return result

# http://stackoverflow.com/questions/8922060/how-to-trace-the-path-in-a-breadth-first-search
def bfs(nodes):
    que = []
    que.append([0])
    end = len(nodes) - 1

    while que:
        print (que)
        u = que.pop(0)
        node = u[-1]
        if node == end:
            return u
        for adjacent in nodes[node]:
            already_in_path =0
            for i in u:
                if i == adjacent:
                    already_in_path = 1
                    break
            if (already_in_path == 1):
                break
            new_path = list(u)
            new_path.append(adjacent)
            que.append(new_path)
'''
def simple_path(nodes):
    queue = []
    queue.append([0])
    end = len(nodes) - 1

    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node == end:
            return path
        for adjacent in nodes[node]:
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)
'''

def main():
    N = 9
    nodes = [[1, 2], [0, 3, 5], [0, 4, 6], [1, 6, 8], [2, 7], [1], [2, 3], [4, 8], [3, 7]]
    graph = {0: [1, 2], 1: [0, 3, 5], 2: [0, 4, 6],  3: [1, 6, 8], 4: [2, 7], 5: [1], 6: [2, 3], 7: [4, 8], 8: [3, 7]}
    # print(simple_path(nodes))
    print(bfs(nodes))
    # print(bfs(graph))

    
if __name__ == "__main__":
    main()
