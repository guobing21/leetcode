# https://www.bilibili.com/video/av84820276?from=search&seid=17476598104352152051

from collections import defaultdict
import heapq

edges = [[0,1,1],[0,3,3],[0,2,6],[2,3,2],[1,2,4],[1,3,5]]#三个元素分别代表起点，终点，权重
n = 4 # 代表图中4个点

def prim(edges, n):
    g = defaultdict(list)
    for e in edges:
        g[e[0]].append((e[1], e[2]))
        g[e[1]].append((e[0], e[2])) # 无向有权图
    q = []
    cost = 0
    seen = set()
    ans = []
    heapq.heappush(q, (0, 0)) # 第二个零代表下一个节点是零节点，第一个零代表到下一个节点节点的权重是零
    for _ in range(n):
        w, v1 = heapq.heappop(q)
        if v1 in seen:
            continue
        cost += w
        ans.append(v1)
        seen.add(v1)
        for v2, w in g[v1]:
            if v2 not in seen:
                heapq.heappush(q, (w, v2))
    return ans, cost


print(prim(edges, 4))


def prim2(edges, n):
    g = defaultdict(list)
    for e in edges:
        g[e[0]].append((e[1], e[2]))
        g[e[1]].append((e[0], e[2])) # 无向有权图
    q = []
    cost = 0
    seen = set()
    ans = []
    heapq.heappush(q, (0, (0, 0)))
    for _ in range(n):
        w, v12 = heapq.heappop(q)
        v1, v2 = v12
        if v2 in seen:
            continue
        cost += w
        ans.append("{} and {}".format(v1, v2))
        seen.add(v2)
        for v, w in g[v2]:
            if v not in seen:
                heapq.heappush(q, (w, (v2,v)))
    return ans, cost

print(prim2(edges, 4))

def kruskal(edges, n):
    # def find_parent(x):
    #     if x != parent[x]:
    #         parent[x] = find_parent(parent[x])
    #     return parent[x]

    def find_parent(x):
        root = x
        while root != parent[root]:
            root = parent[root]
        while x != parent[x]:
            tmp = x
            x = parent[x]
            parent[tmp] = root
        return root



    parent = list(range(n))
    cost = 0
    ans = []
    for v1, v2, w in sorted(edges, key=lambda x: x[2]): # 按照权重排序，先取权重最小的
        v1_parent, v2_parent = find_parent(v1), find_parent(v2)
        if v1_parent == v2_parent: # v1 和v2两个点是联通的
            continue
        parent[v1_parent] = v2_parent
        ans.append("{} and {}".format(v1, v2))
        cost += w
    return ans, cost

print(kruskal(edges, 4))
