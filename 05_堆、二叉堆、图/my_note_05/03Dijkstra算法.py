# https://www.bilibili.com/video/av25829980?from=search&seid=13391343514095937158

# 迪克斯特拉算法，最短路径算法

graph = {
    "A": {"B": 5, "C": 1},
    "B": {"A": 5, "C": 2, "D": 1},
    "C": {"A": 1, "B": 2, "D": 4, "E": 8},
    "D": {"B": 1, "C": 4, "E": 3, "F": 6},
    "E": {"C": 8, "D": 3},
    "F": {"D": 6}
}

# 从dfs演化而来
import heapq
def dijkstra(graph, s):
    pq = []
    heapq.heappush(pq, (0,s)) # 优先队列
    seen = set()
    seen.add(s)
    parent = {s: None}
    distance = {s:0}

    while pq:
        dist, vertex = heapq.heappop(pq)
        seen.add(vertex) # 此处add和图的bfs的add位置不同
        nodes = graph[vertex].keys()
        for w in nodes:
            if w not in seen:
                if dist + graph[vertex][w] < distance.get(w, float("inf")):
                    heapq.heappush(pq, (dist + graph[vertex][w], w))
                    parent[w] = vertex
                    distance[w] = dist + graph[vertex][w]
    return parent, distance

parent, distance = dijkstra(graph, "A")
print(parent)
print(distance)

def get_path(parent, v):
    ans = []
    while v:
        ans.append(v)
        v = parent[v]
    return ans[::-1]

print(get_path(parent, "F"))






