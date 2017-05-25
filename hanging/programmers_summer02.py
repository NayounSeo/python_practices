'''
N : 아파트의 갯수
stations : 현재 4g 기지국의 갯수 -> 5g로 모두 바꿈
w : 기지국이 양 옆으로 도달하는 신호 범위
설치해야할 기지국의 최소 갯수 return하기
정확도 100이지만 속도 0
'''
def solution(N, stations, w):
    aptments = [0 for x in range(N)]
    stations = [x - 1 for x in stations] # due to indexing

    for s in stations:
        build_stations(N, aptments, w, s)

    to_confirm = []
    to_build = 0
    i = 0
    while (i < N):
        if (aptments[i] == 0): # 기지국이 닿지 않는다면
            # 세우기 위해 해야할 행동
            for j in range(i + w, i, -1): # 얼마나 비어있는지 확인
                if (j < N and aptments[j]== 0):
                    # stations.append[j]
                    build_stations(N, aptments, w, j)
                    i = j + w + 1
                    break
            else:
                build_stations(N, aptments, w, i)
                i += w + 1

            to_build += 1

        else: # 이미 기지국이 닿는 다면
            i += 1 # 세워져있는 애를 처음 만났다는 보장이 없다

    return to_build

def build_stations(N, aptments, w, ind):
    from_ind = ind - w if ind - w > 0 else 0
    to_ind = ind + w + 1 if ind + w < N else N
    for i in range (from_ind, to_ind):
        aptments[i] = 1


if __name__ == "__main__":
    '''
    N = 11
    stations = [4, 11]
    w = 1 # answer = 3
    b = solution (N, stations, w)
    print(b)
    print()
    N = 16
    stations = [9]
    w = 2 # answer = 3
    b = solution (N, stations, w)
    print(b)
    print()
    '''
    N = 4
    stations = []
    w = 1 # answer = 3
    b = solution (N, stations, w)
    print(b)