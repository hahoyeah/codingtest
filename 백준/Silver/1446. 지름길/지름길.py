import heapq
import sys
input = sys.stdin.readline

N, D = map(int, input().split())
INF = 1e9

g = {k: [] for k in range(10001)}  # 딕셔너리 형태
# key:value
for _ in range(N):
    u, v, w = map(int, input().split())
    if D >= v:
        g[u].append((v, w))


def dijkstra(graph, start, end):
    d = {k: INF for k in graph}
    for i in range(10001):
        graph[i].append((i+1, 1))

    d[start] = 0
    q = []  # 최소 거리 힙을 저장
    heapq.heappush(q, (0, start))  # 최단 거리가 우선(거리,노드)

    while q:
        # cur_node: 현재 방문중인 노드, cur_cost: 시작노드에서 cur_node까지 비용
        cur_cost, cur_node = heapq.heappop(q)

        if d[cur_node] < cur_cost:
            continue  # 현재 비용이 크면 무시하고 기존걸로 계속 간다. 이 밑을 무시

        # adj_node: 인접노드, weight: 두 노드사이의 가중치
        for adj_node, weight in graph[cur_node]:
            if adj_node <= D:  # 지름길이 도착 지점을 넘어가면 안 됨
                new_cost = weight + cur_cost
                if new_cost < d[adj_node]:
                    d[adj_node] = new_cost  # 더 작은 걸 선택
                    heapq.heappush(q, (new_cost, adj_node))

    return d[end]


result = dijkstra(g, 0, D)
print(result)
