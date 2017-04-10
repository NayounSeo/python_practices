## nodes: list of connected nodes of each node (인접 리스트)
## example: [[1,2],[0,2],[0,1]] for a cyclic graph with 3 nodes
## return: list of nodes in the shortest path
def simple_path(nodes): # 최고 17점..
    start = 0
    end = len(nodes) - 1
    
    # init
    vertex = []
    que = []
    for i in range(end + 1):
        # 정점 번호, 방문 여부 (w/g/b), 가까운 정점, 0으로부터의 거리
        vertex.append([i, 0, 0, 0])
    vertex[0] = [0, 1, -1, 0]
    que.append(vertex[0])
    
    # search
    # TODO : que를 que[i][0], que[i][3]에 따라 정렬하기!
    while (que != []):
        que = sorted(que, key=lambda x:(x[3], x[2]))
        v_s = que[0]
        v = v_s[0] # 정점 번호
        del que[0]

        for edge in nodes[v]:
            if (vertex[edge][1] == 0):
                vertex[edge][1] = 1
                vertex[edge][2] = v
                vertex[edge][3] = vertex[v][3] + 1
                if (edge == end):
                    result = []
                    near_v = end
                    while (near_v != -1):
                        result.append(near_v)
                        near_v = vertex[near_v][2]
                    result = sorted(result)
                    return result
                que.append(vertex[edge])

# http://stackoverflow.com/questions/8922060/how-to-trace-the-path-in-a-breadth-first-search
def bfs(nodes):
    path_que = []
    path_que.append([0])
    end = len(nodes) - 1

    while path_que:
        path = path_que.pop(0) # 현재까지 찾아낸 경로의 경우의 수

        while (True):
            if (check_path (path) == 0):
                break
            path = path_que.pop(0)

        node = path[-1]
        if node == end:
            return path
        for adj in nodes[node]:
            new_path = list(path)
            new_path.append(adj)
            path_que.append(new_path)

def check_path (path):
    result = 0
    if (len(path) < 3):
        return 0
    for i in range(len(path) - 2):
        if (path[i] == path[i + 2]):
            result = 1
            break
    return result

def check_v_in_path (v, path):
    result = 0
    if (len(path) < 3):
        return 0
    for i in range(len(path) - 1):
        if (v == path[i]):
            result = 1
            break
    return result

def main():
    N = 9
    nodes = [[1, 2], [0, 3, 5], [0, 4, 6], [1, 6, 8], [2, 7], [1], [2, 3], [4, 8], [3, 7]]
    graph = {0: [1, 2], 1: [0, 3, 5], 2: [0, 4, 6],  3: [1, 6, 8], 4: [2, 7], 5: [1], 6: [2, 3], 7: [4, 8], 8: [3, 7]}
    print(simple_path(nodes))
    # print(bfs(nodes))
    # print(bfs(graph))

    
if __name__ == "__main__":
    main()
