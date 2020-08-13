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
# def dfs(graph, s):
#     stack = []
#     stack.append(s)
#     seen = set()
#     seen.add(s)
#     while stack:
#         vertex = stack.pop()
#         nodes = graph[vertex]
#         for w in nodes:
#             if w not in seen:
#                 stack.append(w)
#                 seen.add(w)
#         print(vertex)
#
# dfs(graph, "A")

# 2
def dfs(graph, s):
    stack = []
    stack.append(s)
    seen = set()
    seen.add(s)
    ans = []
    while stack:
        vertex = stack.pop()
        ans.append(vertex)
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                stack.append(w)
                seen.add(w)
    return ans

print(dfs(graph, "A"))

