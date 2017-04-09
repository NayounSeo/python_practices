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

def main():
    N = 9
    nodes = [[1, 2], [0, 3, 5], [0, 4, 6], [1, 6, 8], [2, 7], [1], [2, 3], [4, 8], [3, 7]]
    print(simple_path(nodes))
    
if __name__ == "__main__":
    main()
