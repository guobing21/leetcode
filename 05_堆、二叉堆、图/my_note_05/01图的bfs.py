# https://www.bilibili.com/video/BV1Ks411575U

graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E", "F"],
    "E": ["C", "D"],
    "F": ["D"]
}

# 1
# def bfs(graph, s):
#     queue = []
#     queue.append(s)
#     seen = set()
#     seen.add(s)
#     while queue:
#         vertex = queue.pop(0)
#         nodes = graph[vertex]
#         for w in nodes:
#             if w not in seen:
#                 queue.append(w)
#                 seen.add(w)
#         print(vertex)

# bfs(graph, "A")

# # 2 7.164s
# def bfs(graph, s):
#     queue = []
#     queue.append(s)
#     seen = set()
#     seen.add(s)
#     ans = []
#     while queue:
#         vertex = queue.pop(0)
#         ans.append(vertex)
#         nodes = graph[vertex]
#         for w in nodes:
#             if w not in seen:
#                 queue.append(w)
#                 seen.add(w)
#     return ans
#
# print(bfs(graph, "A"))
# for _ in range(1000000):
#     bfs(graph, "A")

# 3 12.944s
# def bfs(graph, s):
#     queue = []
#     queue.append(s)
#     seen = set()
#     seen.add(s)
#     ans = []
#     while queue:
#         vertex = queue.pop(0)
#         if vertex in ans:
#             continue
#         seen.add(vertex)
#         ans.append(vertex)
#         nodes = graph[vertex]
#         for w in nodes: # 加慢了程序：其实加入了重复节点了，只是加入了以后pop(0)以后发现有重复及时停止了，但其实queue里是有重复节点的。
#             queue.append(w)
#     return ans
#
# print(bfs(graph, "A"))
# for _ in range(1000000):
#     bfs(graph, "A")

# 4
# 4.1 加入partent映射
def bfs(graph, s):
    queue = []
    queue.append(s)
    seen = set()
    seen.add(s)
    ans = []
    parent = {s: None}
    while queue:
        vertex = queue.pop(0)
        ans.append(vertex)
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                queue.append(w)
                seen.add(w)
                parent[w] = vertex
    return ans, parent

# print(bfs(graph, "A"))

# 4.2 找到到达某点的bfs路径
def get_path(parent, v):
    ans = []
    while v:
        ans.append(v)
        v = parent[v]
    return ans[::-1]

_, parent = bfs(graph, "A")
print(get_path(parent, "D"))

