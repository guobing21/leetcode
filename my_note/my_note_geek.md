**算法训练营**

# 0 课前准备

## 0.1 git快速使用

**眼过千遍，不如手过一遍**

### 0.1.1 初始化配置

**1 本地仓库初始化配置**

```shell
# 1 配置姓名
$ git config --global user.name "username"
# 2 配置真实邮箱
$ git config --global user.email "...@..."
# 3 查看配置信息
$ git config --global --list
# 或
$ git config --list
```

--system是系统级配置信息

--global 登录用户全局级的配置

--local是仓库级别的配置，不写默认是--local

优先级递增，同样的配置，优先级高的配置会覆盖优先级低的
所以通常，对所有用户都通用的配置放在system，对某个独立用户的共用项放在global，对某个仓库特殊的配置放在local。

**2  远程仓库初始化配置**

1 建议使用SSH协议而不是HTTPS协议

SSH协议第一次配置公私钥比较麻烦，但是以后会比较方便

HTTPS会每次都输入用户名密码

ps：

​	虽然使用了HTTPS协议输入以下命令也可以避免每次输入用户名和密码，但是不建议这么做，因为是用明文的方式将用户名和密码保存到了本地。

​	但是如果是mac，又可以使用HTTPS协议。

```shell
$ git config --global credential.helper store
```

2 将本地已存在的仓库添加到远程仓库

在本地仓库路径下的终端中输入

```shell
$ git remote add origin ...
```

3 生成公私钥 

```shell
$ ssh-keygen -t rsa -C "配置时的邮箱"
```

生成 id_rsa 和 id_rsa.pub 两个文件

将id_rsa.pub内容粘贴到github 中的setting--》SSH and GPG keys --》 NEW SSH key --》 Key，title可以不用写，最后点击add ssh key

4 测试能否和远程仓库连接

```shell
$ ssh -T git@github.com
```

### 0.1.2 常用git命令

```shell
$ git status
$ git add .
$ git commit -m "version info"
$ git log
$ git push -u origin master
```

## 0.2 高效学习算法训练营

**三分看视频理解，七分练习**

### 0.2.1 视频

​		最好方法：1.5-2.0倍速播放，难点暂停反复看

​		最差方法： 原速看完，仅一遍，像看美剧

​		就像keep健身一样，反复看，反复练

### 0.2.2 习惯

​		最好：

​					不要死磕，10-15分钟做不出来放弃，敢于背正确代码；

​					多过遍数，五毒神掌；

​					不懒于看国际版高手代码。不能仅AC了事，要看高票和高质量题解（君子性非异也善假于物也）

​		最差： 

​				一道题死磕2-3小时，没有精力了；

​				题目只做一遍（90%素人，30%学员）

# 1 数据结构与算法总览

精通一个领域，职业训练需要三步：拆分知识点，刻意练习，反馈

## 0.1 Chunk it up 切碎知识点

### 0.1.1 数据结构

​		**一维:**

​				基础：数组array（string），链表linked list

​				高级：栈stack，队列queue，双端队列deque，集合set，映射map（hash or map）

​		**二维：**

​				基础：树tree，图graph

​				高级：二叉搜索树binary search tree（红黑树red-black tree，AVL），堆heap，并查集disjoint set，							字典树Trie

​		 **特殊：**

​				位运算Bitwise，布隆过滤器BloomFilter

​				LRU Cache

### 0.1.2 算法

​		**基础：**

​				选择语句 branch

​				循环语句 iteration

​				递归语句 Recursion(Divide & Conquer, Backtrace)(分治，回溯)

​		**高级：** 

​				搜索（深度优先搜索Depth first search，广度优先搜索Breadth first search，启发式搜索A*）

​				动态规划Dynamic Programming

​				二分查找Binary Search

​				贪心 Greedy

​				数学Math, 几何Geometry

​	**头脑中能想到每种算法的思想和模板**

## 0.2 Deliberate Practicing 刻意练习

### 0.2.1 五毒神掌

​		1 第一遍：5分钟读题和思考；10-15分钟做不出来直接看答案，多对比解法优劣；背诵并默写好的解法。

​		2 第二遍： 不看答案自己写；对比多种解法，能否优化？

​		3 第三遍：24小时之后，复习

​		4 第四遍：一周之后复习

​		5 第五遍：面试前1-2周复习

​		**最大误区是只做一遍**

### 0.2.2 多练习缺陷，弱点地方

​		不爽的时候是因为在成长，就像健身房的肌肉酸痛是在长肌肉！

### 0.2.3 面试切题方法4件套

1 确保准确理解题目要求，可以和面试官沟通 Clarification

2 多想可能解法，对比他们的时空复杂度 Possible solutions

3 写coding

4 给出几个测试用例

## 0.3 Feedback 反馈

1 即时反馈

2 主动型反馈（GitHub， leetcode）

3 被动式反馈（code review）

# 2 训练准备和复杂度分析

## 2.1 训练环境设置、编码技巧和Code Style

### 2.1.1 常用工具配置

​		1 用chrome浏览器，且默认Google搜索引擎

​		2 mac: iTerm2 + zsh(oh my zsh)

​			win: Microsoft new terminal

​		3  vscode, Java：intellJ(不要用Eclipse)，Python：Pycharm

​		4 LeetCode plugin插件

​		5 mac下让打字速度最快延迟最小：搜索keyboard--》Key Repeat跳到Fast，Delay Until Repeat 调到Short

### 2.1.2 Code Style

​	Google code style

​	Facebook

​	Airbnb

### 2.2.3 快捷键

​		跳到行头行尾: command + left/right

​		删除光标右侧：fn + delete

​		光标按单词切分: option + left/right

​		选中整行： shift + commoand + right

​		快速创建一个函数: mac下：option + return，win下：alt + enter  

​		打开最近文件: command E

​		搜索： top tips pycharm 使用技巧 best practices

### 2.2.4  自顶向下的编程方式

​		最关键的逻辑放到最上面，细节放到最后面

​		例如新闻标题和新闻细节

​		《clean code》

## 2.2  时间复杂度和空间复杂度分析

### 2.2.1 Big O notation

O(1): Constant Complexity 常数复杂度

O(logn): Logarithmic Complexity 对数复杂度

O(n): Linear Complexity 线性时间复杂度

O(n^2): N square Complexity 平方

O(n^3): N cubic Complexity 立方

O(2^n): Exponential Growth  指数

O(n!): Faxtorial 阶层

注意：只看最高复杂度的运算

### 2.2.2 时间复杂度

递归

​		主定理 master Theorem

​		以下四种情况需要记住

​		排好序二分查找：O（log2（n）） 

​		二叉树遍历： O（n）(简化思考：每个节点都访问一次，因此是O（n）)

​		排好序二维矩阵二分查找：O（n）

​		归并排序： O（nlogn）

![](E:\my_note\09_geek\my_note\note_images\5.png)

![](E:\my_note\09_geek\my_note\note_images\1.png)

###  2.2.3 空间复杂度

​		两条原则：

​			1 数组的长度

​            2 递归的深度

​		取最大值

# 3 数组、链表、跳表

## 3.1 数组 array

由于有  内存管理器，访问数组中第一个元素和任意其他的元素的时间复杂度都是一样的O(1)。

查找快，头尾删除插入快，中间插入删除慢

## 3.2 链表 linked list

任意位置插入删除都快，遍历查找慢

LRU cache用的是多链表实现的

## 3.3 跳表 skip list

跳表的使用只能用于元素有序的情况。

redis 用的是跳表而不是红黑树。

升维思想+空间换时间

算是综合了数组和链表，查找速度从链表的O（n）提升到了O（logn）

空间复杂度为n + n/2 + n/4 +...+2= n(1+1/2+1/4+1/0.5n),收敛的等比数列，为kn，总之空间复杂度为O（n），但是肯定比链表多一些。

![](E:\my_note\09_geek\my_note\note_images\6.png)

## 3.4 时空对比

|      | 查找元素时间复杂度 | 头尾增删元素时间复杂度 | 中间位置增删元素时间复杂度 | 空间复杂度 |
| ---- | ------------------ | ---------------------- | -------------------------- | ---------- |
| 数组 | **O（1）**         | O（1）                 | **O（n）**                 | **O(n)**   |
| 链表 | **O(n)**           | O(1)                   | **O(1)**                   | **O(n)**   |
| 跳表 | **O(log2n)**       | O(1)                   | **O(log2n)**               | **O(n)**   |

# 4 栈和队列的实现与特性

## 4.1 栈 stack

​	后进先出 Last in -  First out（LIFO）

​	先进后出 First in - Last out (FILO)

​	增加删除操作为O（1），查询为O（n）（因为是无序的）

## 4.2 队列 queue

​	先进先出 First in - First out (FIFO)

​	后进后出 Last in - Last out(LILO)

​	增加删除操作为O（1），查询为O（n）（因为是无序的）

## 4.3 deque：Double-End Queue 双端队列

​	栈和队列的结合体

​	两端都可以进出

​	插入删除操作为O（1），查询为O（n）（因为是无序的）

## 4.4 Priority Queue 优先队列

​	插入O（1）

​	取出O（logN）按照元素的优先级取出

​	底层具体实现的数据结构较为多样和复杂：各种各样的堆heap，各种二叉搜索树BST(binary search tree)（例如AVL，红黑树）, treap

​	python的优先队列用heapq 接口实现

​	高性能的container库，里面有deque

## 4.5  队列，双端队列，优先队列，堆的python相关库

​	队列 queue.Queue（）

​	双端队列 collections.deque（）

​	优先队列 （最小值）queue.PriorityQueue（）

​	堆（小顶堆） heapq

​	collections库下有：deque, Counter, defaultdict

# 5 哈希表，映射，集合

1 哈希表 Hash table

2 哈希函数，散列函数 Hash Function

3 哈希碰撞：解决方法可以是拉链式解决方法，不在存一个数，而是链表

4 哈希函数一般情况下，增删查都是O（1）的，但最坏情况下若哈希函数选的特别不好，就退化成链表O（n）

# 6 树，堆，图

## 6.1 树

1 树没有环，图有环

2 可以这么认为：链表是特殊化的树（只有一个子节点），树是特殊化的图（没有环的图）

3 单链表增删为O（1），但查询为为O（n）

## 6.2 二叉树

1 遍历顺序

​	前序pre-order：根左右

​	中序in-order： 左根右

​	后续post-order：左右根

```python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class BinaryTree:
    def __init__(self, root):
        self.path = []
    
    def preorder(self, root):
        if root:
            self.path.append(root.val)
            self.preorder(root.left)
            self.preorder(root.right)
    
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            self.path.append(root.val)
            self.inorder(root.right)
            
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            self.path.append(root.val)
```

2 二叉树遍历最适合递归，当然也可以像广度优先遍历一样使用循环遍历，但是比较麻烦。

3  前序遍历：深度优先搜索（笼统说，前中后序遍历都是深度优先）

​	层序遍历：广度优先

4 递归实现树的遍历对比：

|      | 法一（两个位） | 法二（两个while）（不适用N叉树） | 法三（1个while） |
| ---- | -------------- | -------------------------------- | ---------------- |
| 前序 | 右左根         | 根左右                           | 右左根           |
| 中序 | 右左根         | 左根右                           | 无               |
| 后序 | 根右左         | 根右左（res反）                  | 左右根（res反）  |



## 6.3 二叉搜索树Binary Search Tree

1 二叉搜索树的查询为O（logn），不在是链表或普通树的O（n），相当于加速了，其他操作也是O（logn）

2 左子树所有节点小于根节点，右子树所有节点大于根节点，以此类推。注意是所有节点而不只是左右儿子。

3 二叉搜索树的中序遍历是升序遍历。

https://visualgo.net/en

4 树的面试题经常用递归解法，为什么？(课外找的)

​	1） 除了暴力解法之外，优秀算法的本质是寻找重复子单元，然后加入到loop循环，或者递归中；
​	2） 树的节点（根节点，左子节点，右子节点）很显然是典型的重复子单元；
​	3） 相对于循环来讲，递归更符合人的逻辑思考；
​	4） 而实际上，在实际工程应用中，更倾向于使用循环而非递归，原因是担心栈溢出

## 6.4 堆 Heap

1 堆：可以迅速找到一堆数中的最大值或最小值的结构（python自带小顶堆）

2 常见的堆是二叉堆和斐波那契堆（斐波那契堆工程上更多，效果更好，这里不用会实现）

3 二叉堆只是堆的一种，有很多种类的堆(就像优先队列可以用堆实现，也可以用红黑树等各种各样的结构实现)

4 堆的时间复杂度

以大顶堆为例：

find-max: O(1)

delete-max: O(logN)

insert(create): O(logN) or O(1)（斐波那契堆）

建堆的时间复杂度是O(n)

## 6.5 二叉堆

1 通过完全二叉树来实现（注意：不是二叉搜索树）（二叉搜索树是根节点大于左子树，小于右子树。而这里，任意节点的值都是大于等于所有的子节点，而不仅仅是左节点）

2 性质：

​	1）是一个完全树（除了子节点，其他节点都是满的）

​	2）树中任意节点的值总是>=子节点的值（和二叉搜索树不同）

3  如果非要用二叉搜索树实现堆，那么增加删除操作确实也是O（logn），但是find-max操作就从O（1）变为O（logn）了。

4

![](E:\my_note\09_geek\my_note\note_images\7.png)

5 二叉堆只是一种常见且简单实现的堆，但并不是最优的实现。实际工程并不使用二叉堆，而是直接使用优先队列（priority queue）（这里的优先队列就不一定是二叉堆了，可能是其他种类的堆）（Python中的heapq库）

## 6.6 图

### 6.6.1 图的属性和分类

1 有点（vertex）有边（edge）

2 邻接矩阵和邻接边

3 无向无权图：关于对角线对称，非0即1

​	有向无权图：非0即1

​	无向有权图：关于对角线对称

​	有向有权图

### 6.6.2 基于图的相关算法

#### 1 图的dfs和bfs模板

bfs算法和树的最大的区别是，树可以不写visited=set()，但是图中必须要写。因为树中无环，图中可能有环。

```python
# dfs
visited = set() #和树中的dfs最大区别
def dfs(node, visited):
    if node in visited: # terminator
    	# already visited 
    	return 
	visited.add(node) 
	# process current node here. 
	...
	for next_node in node.children(): 
		if next_node not in visited: 
			dfs(next_node, visited)
```

```python
# bfs
def BFS(graph, start, end):
    visited = set() #和树中的bfs最大区别
	queue = [] 
	queue.append([start]) 
	while queue: 
		node = queue.pop() 
		visited.add(node)
		process(node) 
		nodes = generate_related_nodes(node) 
		queue.push(nodes)
	# other processing work 
	...
```

#### 2 图的bfs

```python
graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E", "F"],
    "E": ["C", "D"],
    "F": ["D"]
}

def bfs(graph, s):
    queue = []
    queue.append(s)
    seen = set()
    seen.add(s)
    ans = []
    while queue:
        vertex = queue.pop(0)
        ans.append(vertex)
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                queue.append(w)
                seen.add(w)
    return ans

def bfs(graph, s):
    queue = []
    queue.append(s)
    seen = set()
    seen.add(s)
    ans = []
    while queue:
        vertex = queue.pop(0)
        if vertex in ans:
            continue
        seen.add(vertex)
        ans.append(vertex)
        nodes = graph[vertex]
        for w in nodes: # 加慢了程序：其实加入了重复节点了，只是加入了以后pop(0)以后发现有重复及时停止了，但其实queue里是有重复节点的。
            queue.append(w)
    return ans
```

#### 3 图的dfs

```python
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
```

#### 4 Dijkstra算法，迪克斯特拉算法，最短路径算法

```python
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
```

#### 5 最小生成树Prim算法和Kruskal算法

```python
from collections import defaultdict
import heapq

edges = [[0,1,1],[0,3,3],[0,2,6],[2,3,2],[1,2,4],[1,3,5]]#三个元素分别代表起点，终点，权重
n = 4 # 代表图中4个点

def prim(edges, n):
    g = defaultdict(list)
    for e in edges:
        g[e[0]].append((e[1], e[2]))
        g[e[1]].append((e[0], e[2]))
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


def kruskal(edges, n):
    # def find_parent(x):
    #     if x != parent[x]:
    #         parent[x] = find_parent(parent[x])
    #     return parent[x]

    def find_parent(x): # 并查集
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
    for v1, v2, w in sorted(edges, key=lambda x: x[2]): # 安装权重排序，先取权重最小的
        v1_parent, v2_parent = find_parent(v1), find_parent(v2)
        if v1_parent == v2_parent: # v1 和v2两个点是联通的
            continue
        parent[v1_parent] = v2_parent
        ans.append("{} and {}".format(v1, v2))
        cost += w
    return ans, cost

print(kruskal(edges, 4))
```



# 7 泛型递归、树的递归

## 7.1 递归模板

归去来兮

```python
def recursion(level, param1, param2, ...): 
    # recursion terminator  1递归终止条件
    if level > MAX_LEVEL: 
	   process_result 
	   return 
    # process logic in current level 2 处理当层逻辑
    process(level, data...) 
    # drill down 3 下到下一层
    self.recursion(level + 1, p1, ...) 
    # reverse the current level status if needed 4 清理当前层状态
```

```java
public void recur(int level, int param) { 

 // terminator 
 if (level > MAX_LEVEL) { 
  // process result 
  return; 
 }

 // process current logic 
 process(level, param); 

 // drill down 
 recur( level: level + 1, newParam); 

 // restore current status 
}
```

## 7.2 递归步骤

1 recursion terminator 终结条件

2 process logic in current level  处理这一层

3 drill down 进入下一层

4 reverse the current level status if needed 如果需要的话，清理本层变量

## 7.3 思维要点

1 抵制人肉递归

2 找最近重复子问题

3 数学归纳法思维

# 8 分治、回溯

## 8.1 分治 divide and conquer

1 分治和回溯是一种特殊的、复杂的递归

2 找重复性（分解（split）成子问题）

​	最近重复性：分治，回溯等递归

​	最优重复性：动态规划

3 分治与泛型递归最大的不同是，分治要把得到的子的结果进行组合合并（merge）

4 分治代码模板

```python
# Python
def divide_conquer(problem, param1, param2, ...): 
  # recursion terminator 
  if problem is None: 
	print_result 
	return 
  # prepare data 
  data = prepare_data(problem) 
  subproblems = split_problem(problem, data) 
  # conquer subproblems 
  subresult1 = self.divide_conquer(subproblems[0], p1, ...) 
  subresult2 = self.divide_conquer(subproblems[1], p1, ...) 
  subresult3 = self.divide_conquer(subproblems[2], p1, ...) 
  …
  # process and generate the final result 
  result = process_result(subresult1, subresult2, subresult3, …)
	
  # revert the current level states
```

## 8.2 回溯 Backtracking

1 采用试错的思想

2 不断的再每一层去尝试，

3 典型应用：八皇后，数独，括号生成（尽早判断括号合不合法）

4 最差情况下时间复杂度指数级

# 9 深度优先搜索和广度优先搜索

## 9.1 dfs模板

**递归写法**

```python
visited = set() 
def dfs(node, visited):
    if node in visited: # terminator
    	# already visited 
    	return 
	visited.add(node) 
	# process current node here. 
	...
	for next_node in node.children(): 
		if next_node not in visited: 
			dfs(next_node, visited)
```

```python
visited = set() 
def dfs(node, visited):
	visited.add(node) 
	# process current node here. 
	...
	for next_node in node.children(): 
		if next_node not in visited: 
			dfs(next_node, visited)
```

```python
visited = set() 
def dfs(node):
    if node in visited: # terminator
    	# already visited 
    	return 
	visited.add(node)  
	# process current node here. 
	...
	dfs(node.left)
    dfs(node.right)
```

**非递归写法**

关键利用了栈stack后进先出的性质

```python
def DFS(self, tree): 
	if tree.root is None: 
		return [] 
	visited, stack = [], [tree.root]
	while stack: 
		node = stack.pop() 
		visited.add(node)
		process (node) 
		nodes = generate_related_nodes(node) 
		stack.push(nodes) 
	# other processing work 
	...
```

## 9.2 bfs模板

利用了队列queue的先入先出的性质

最短路径问题中，广度优先一般是对的，而深度优先得到的第一个答案还不一定是对的

```python
# Python
def BFS(graph, start, end):
    visited = set()
	queue = [] 
	queue.append([start]) 
	while queue: 
		node = queue.pop(0) 
		visited.add(node)
		process(node) 
		nodes = generate_related_nodes(node) 
		queue.push(nodes)
	# other processing work 
	...
```

# 10 贪心算法Greedy

1 希望通过每一步的最优导致全局最优

2 

| 方法     | 描述                         |
| :------- | ---------------------------- |
| 贪心     | 当下做局部最优判断，不能回退 |
| 回溯     | 能够回退                     |
| 动态规划 | 最优判断+能够回退            |

3 最小生成树，霍夫曼编码等使用

4 贪心一般不能求得所要的答案，但是如果可以通过贪心算法解决一般都是最好的办法。一般用来辅助求解，或解决一些要求精度不高的问题。

# 11 二分查找

## 11.1 二分查找前提

1 目标函数单调递增或递减（有序的）

2 存在上下界（bounded）

3 能够通过索引访问（index accessible）（单链表不好用二分查找，除非把单链表改造成跳表等）

## 11.2 二分查找模板

```Python
# Python
left, right = 0, len(array) - 1 
while left <= right: 
	  mid = (left + right) / 2 
	  if array[mid] == target: 
		    # find the target!! 
		    break or return result 
	  elif array[mid] < target: 
		    left = mid + 1 
	  else: 
		    right = mid - 1
```

# 12 动态规划

## 12.1 动态规划知识点

1 将复杂问题分解为子问题，寻找重复性

2 分治、回溯、递归、动态规划等没有本质区别

3 数学归纳法

4 本质：寻找重复性 

5 DP关键点：

​	1）动态规划和递归或者分治没有根本上的区别，关键看有无最优子结构

​	2） 共性：找到重复子问题

​	3）差异性：最优子结构、中途可以淘汰次优解（不淘汰的话会是指数级的时间复杂度，淘汰的话一般会变成n^2,或n）

6 麻省理工教程、算法导论、大学课本

## 12.2 递归代码模板

```python
# Python
def recursion(level, param1, param2, ...): 
    # recursion terminator 
    if level > MAX_LEVEL: 
	   process_result 
	   return 
    # process logic in current level 
    process(level, data...) 
    # drill down 
    self.recursion(level + 1, p1, ...) 
    # reverse the current level status if needed
```



```java
// Java
public void recur(int level, int param) { 
  // terminator 
  if (level > MAX_LEVEL) { 
    // process result 
    return; 
  }
  // process current logic 
  process(level, param); 
  // drill down 
  recur( level: level + 1, newParam); 
  // restore current status 
 
}
```

## 12.3 分治代码模板

```Python
# Python
def divide_conquer(problem, param1, param2, ...): 
  # recursion terminator 
  if problem is None: 
	print_result 
	return 
  # prepare data 
  data = prepare_data(problem) 
  subproblems = split_problem(problem, data) 
  # conquer subproblems 
  subresult1 = self.divide_conquer(subproblems[0], p1, ...) 
  subresult2 = self.divide_conquer(subproblems[1], p1, ...) 
  subresult3 = self.divide_conquer(subproblems[2], p1, ...) 
  …
  # process and generate the final result 
  result = process_result(subresult1, subresult2, subresult3, …)
	
  # revert the current level states
```

# 13 字典树和并查集

## 13.1 Trie 树代码模板

```python
# Python 
class Trie(object):
  
	def __init__(self): 
		self.root = {} 
		self.end_of_word = "#" 
 
	def insert(self, word): 
		node = self.root 
		for char in word: 
			node = node.setdefault(char, {}) 
		node[self.end_of_word] = self.end_of_word 
 
	def search(self, word): 
		node = self.root 
		for char in word: 
			if char not in node: 
				return False 
			node = node[char] 
		return self.end_of_word in node 
 
	def startsWith(self, prefix): 
		node = self.root 
		for char in prefix: 
			if char not in node: 
				return False 
			node = node[char] 
		return True
```

```c++
//C/C++
class Trie {
    struct TrieNode {
        map<char, TrieNode*>child_table;
        int end;
        TrieNode(): end(0) {}
    };
        
public:
    /** Initialize your data structure here. */
    Trie() {
        root = new TrieNode();
    }
    
    /** Inserts a word into the trie. */
    void insert(string word) {
        TrieNode *curr = root;
        for (int i = 0; i < word.size(); i++) {
            if (curr->child_table.count(word[i]) == 0)
                curr->child_table[word[i]] = new TrieNode();
                
            curr = curr->child_table[word[i]];                
        }
        curr->end = 1;
    }
    
    /** Returns if the word is in the trie. */
    bool search(string word) {
        return find(word, 1);
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(string prefix) {
        return find(prefix, 0);
    }
private:
    TrieNode* root;
    bool find(string s, int exact_match) {
        TrieNode *curr = root;
        for (int i = 0; i < s.size(); i++) {
            if (curr->child_table.count(s[i]) == 0)
                return false;
            else
                curr = curr->child_table[s[i]];
        }
        
        if (exact_match)
            return (curr->end) ? true : false;
        else
            return true;
    }
};
```

```java
//Java
class Trie {
    private boolean isEnd;
    private Trie[] next;
    /** Initialize your data structure here. */
    public Trie() {
        isEnd = false;
        next = new Trie[26];
    }
    
    /** Inserts a word into the trie. */
    public void insert(String word) {
        if (word == null || word.length() == 0) return;
        Trie curr = this;
        char[] words = word.toCharArray();
        for (int i = 0;i < words.length;i++) {
            int n = words[i] - 'a';
            if (curr.next[n] == null) curr.next[n] = new Trie();
            curr = curr.next[n];
        }
        curr.isEnd = true;
    }
    
    /** Returns if the word is in the trie. */
    public boolean search(String word) {
        Trie node = searchPrefix(word);
        return node != null && node.isEnd;
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    public boolean startsWith(String prefix) {
        Trie node = searchPrefix(prefix);
        return node != null;
    }

    private Trie searchPrefix(String word) {
        Trie node = this;
        char[] words = word.toCharArray();
        for (int i = 0;i < words.length;i++) {
            node = node.next[words[i] - 'a'];
            if (node == null) return null;
        }
        return node;
    }
}
```

## 13.2 并查集模板

```python
# Python 
def init(p): 
	# for i = 0 .. n: p[i] = i; 
	p = [i for i in range(n)] 
 
def union(self, p, i, j): 
	p1 = self.parent(p, i) 
	p2 = self.parent(p, j) 
	p[p1] = p2 
 
def parent(self, p, i): 
	root = i 
	while p[root] != root: 
		root = p[root] 
	while p[i] != i: # 路径压缩 ?
		x = i; i = p[i]; p[x] = root 
	return root

# 或
def parent(self, p, i): 
    if p[i] != i:
        p[i] = self.parent(self, p, p[i])
    return i   
```

```java
// Java
class UnionFind { 
	private int count = 0; 
	private int[] parent; 
	public UnionFind(int n) { 
		count = n; 
		parent = new int[n]; 
		for (int i = 0; i < n; i++) { 
			parent[i] = i;
		}
	} 
	public int find(int p) { 
		while (p != parent[p]) { 
			parent[p] = parent[parent[p]]; 
			p = parent[p]; 
		}
		return p; 
	}
	public void union(int p, int q) { 
		int rootP = find(p); 
		int rootQ = find(q); 
		if (rootP == rootQ) return; 
		parent[rootP] = rootQ; 
		count--;
	}
}
```



```c++
//C/C++
class UnionFind {
public:
    UnionFind(vector<vector<char>>& grid) {
        count = 0;
        int m = grid.size();
        int n = grid[0].size();
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == '1') {
                    parent.push_back(i * n + j);
                    ++count;
                }
                else {
                    parent.push_back(-1);
                }
                rank.push_back(0);
            }
        }
    }

//递归
    int find(int i) {
        if (parent[i] != i) {
            parent[i] = find(parent[i]);
        }
        return parent[i];
    }


    void unite(int x, int y) {
        int rootx = find(x);
        int rooty = find(y);
        if (rootx != rooty) {
            if (rank[rootx] < rank[rooty]) {
                swap(rootx, rooty);
            }
            parent[rooty] = rootx;
            if (rank[rootx] == rank[rooty]) rank[rootx] += 1;
            --count;
        }
    }


    int getCount() const {
        return count;
    }


private:
    vector<int> parent;
    vector<int> rank;
    int count;
};
```

# 14 高级搜索

## 14.1 A*模板

```python
# Python
def AstarSearch(graph, start, end):
	pq = collections.priority_queue() # 优先级 —> 估价函数
	pq.append([start]) 
	visited.add(start)
	while pq: 
		node = pq.pop() # can we add more intelligence here ?
		visited.add(node)
		process(node) 
		nodes = generate_related_nodes(node) 
   unvisited = [node for node in nodes if node not in visited]
		pq.push(unvisited)
```

```java
//Java
	public class AStar
	{
		public final static int BAR = 1; // 障碍值
		public final static int PATH = 2; // 路径
		public final static int DIRECT_VALUE = 10; // 横竖移动代价
		public final static int OBLIQUE_VALUE = 14; // 斜移动代价
		
		Queue<Node> openList = new PriorityQueue<Node>(); // 优先队列(升序)
		List<Node> closeList = new ArrayList<Node>();
		
		/**
		 * 开始算法
		 */
		public void start(MapInfo mapInfo)
		{
			if(mapInfo==null) return;
			// clean
			openList.clear();
			closeList.clear();
			// 开始搜索
			openList.add(mapInfo.start);
			moveNodes(mapInfo);
		}
	

		/**
		 * 移动当前结点
		 */
		private void moveNodes(MapInfo mapInfo)
		{
			while (!openList.isEmpty())
			{
				Node current = openList.poll();
				closeList.add(current);
				addNeighborNodeInOpen(mapInfo,current);
				if (isCoordInClose(mapInfo.end.coord))
				{
					drawPath(mapInfo.maps, mapInfo.end);
					break;
				}
			}
		}
		
		/**
		 * 在二维数组中绘制路径
		 */
		private void drawPath(int[][] maps, Node end)
		{
			if(end==null||maps==null) return;
			System.out.println("总代价：" + end.G);
			while (end != null)
			{
				Coord c = end.coord;
				maps[c.y][c.x] = PATH;
				end = end.parent;
			}
		}
	

		/**
		 * 添加所有邻结点到open表
		 */
		private void addNeighborNodeInOpen(MapInfo mapInfo,Node current)
		{
			int x = current.coord.x;
			int y = current.coord.y;
			// 左
			addNeighborNodeInOpen(mapInfo,current, x - 1, y, DIRECT_VALUE);
			// 上
			addNeighborNodeInOpen(mapInfo,current, x, y - 1, DIRECT_VALUE);
			// 右
			addNeighborNodeInOpen(mapInfo,current, x + 1, y, DIRECT_VALUE);
			// 下
			addNeighborNodeInOpen(mapInfo,current, x, y + 1, DIRECT_VALUE);
			// 左上
			addNeighborNodeInOpen(mapInfo,current, x - 1, y - 1, OBLIQUE_VALUE);
			// 右上
			addNeighborNodeInOpen(mapInfo,current, x + 1, y - 1, OBLIQUE_VALUE);
			// 右下
			addNeighborNodeInOpen(mapInfo,current, x + 1, y + 1, OBLIQUE_VALUE);
			// 左下
			addNeighborNodeInOpen(mapInfo,current, x - 1, y + 1, OBLIQUE_VALUE);
		}
	

		/**
		 * 添加一个邻结点到open表
		 */
		private void addNeighborNodeInOpen(MapInfo mapInfo,Node current, int x, int y, int value)
		{
			if (canAddNodeToOpen(mapInfo,x, y))
			{
				Node end=mapInfo.end;
				Coord coord = new Coord(x, y);
				int G = current.G + value; // 计算邻结点的G值
				Node child = findNodeInOpen(coord);
				if (child == null)
				{
					int H=calcH(end.coord,coord); // 计算H值
					if(isEndNode(end.coord,coord))
					{
						child=end;
						child.parent=current;
						child.G=G;
						child.H=H;
					}
					else
					{
						child = new Node(coord, current, G, H);
					}
					openList.add(child);
				}
				else if (child.G > G)
				{
					child.G = G;
					child.parent = current;
					openList.add(child);
				}
			}
		}
	

		/**
		 * 从Open列表中查找结点
		 */
		private Node findNodeInOpen(Coord coord)
		{
			if (coord == null || openList.isEmpty()) return null;
			for (Node node : openList)
			{
				if (node.coord.equals(coord))
				{
					return node;
				}
			}
			return null;
		}
	

	

		/**
		 * 计算H的估值：“曼哈顿”法，坐标分别取差值相加
		 */
		private int calcH(Coord end,Coord coord)
		{
			return Math.abs(end.x - coord.x)
					+ Math.abs(end.y - coord.y);
		}
		
		/**
		 * 判断结点是否是最终结点
		 */
		private boolean isEndNode(Coord end,Coord coord)
		{
			return coord != null && end.equals(coord);
		}
	

		/**
		 * 判断结点能否放入Open列表
		 */
		private boolean canAddNodeToOpen(MapInfo mapInfo,int x, int y)
		{
			// 是否在地图中
			if (x < 0 || x >= mapInfo.width || y < 0 || y >= mapInfo.hight) return false;
			// 判断是否是不可通过的结点
			if (mapInfo.maps[y][x] == BAR) return false;
			// 判断结点是否存在close表
			if (isCoordInClose(x, y)) return false;
	

			return true;
		}
	

		/**
		 * 判断坐标是否在close表中
		 */
		private boolean isCoordInClose(Coord coord)
		{
			return coord!=null&&isCoordInClose(coord.x, coord.y);
		}
	

		/**
		 * 判断坐标是否在close表中
		 */
		private boolean isCoordInClose(int x, int y)
		{
			if (closeList.isEmpty()) return false;
			for (Node node : closeList)
			{
				if (node.coord.x == x && node.coord.y == y)
				{
					return true;
				}
			}
			return false;
		}
	}
```



# 15 红黑树和AVL树

## 15.1  AVL树

1 平衡二叉树搜索

2 每个节点存平衡因子{-1， 0， 1}

3 四种旋转操作：

​	左左子树：右旋

​	右右子树：左旋

​	左右子树：左右旋

​	右左子树：右左旋

## 15.2 红黑树

近似平衡的二叉搜索树

任意一个结点的左右子树的高度差小于两倍

1 每个节点不是红色就是黑色

2 根节点是黑色

3 每个叶节点（NIL节点，空节点）是黑色

4 不能有相邻接的两个红色节点

5 从任一节点到其每个叶子节点的所有路径都包含相同数目的黑色节点（从根到叶子的最长可能路径不多于最短的可能路径的两倍长）

## 15.3 红黑树和AVL树对比

AVL树，平衡二叉搜索树，搜索速度快，插入删除操作费时，适合读

红黑树，近似二叉搜索树，插入删除相对快，适合写

1  因为AVL树比红黑树更加严格平衡，所以AVL树查询操作更快。

2  因为红黑树对平衡要求相对宽松，使得红黑树的旋转操作更少，所以红黑树的插入删除操作更快。

3 对于每个结点来说，AVL树要存储平衡因子和高度，需要使用一个整数，而红黑树只需存储是红还是黑这一个bit的数据。（大量的结点中，红黑树更省存储空间）

4  读操作多，写操作少的地方，多使用AVL树（数据库db中，例如微博看的多，写得少）

​	插入操作多的地方，多使用红黑树，例如高级语言的库中，（java，c++的map，set，dict中）

# 16 位运算

## 16.1 与、或、非、异或的符号

与 &

或 |

非 ~

异或^

## 16.2 异或特点

不同为1，相同为0

```Python
x ^ 0 = x
x ^ 1s = ~x #1s = -0
x ^ (-x) = 1s # 全1
x ^ x = 0
c = a ^ b => a ^ c = b => b ^ c = a #交换律
a ^ b ^ c = a ^ (b^c) = (a^b)^c # 结合律
```

## 16.3 指定位置的位运算

1 将x最右边的n位清零

```python
x & (~0<<n)
```

2 获取x的第n位的值（0或1）

```Python
(x>>n)&1
```

3 获取x的第n位幂值

```Python
x&(1<<n)
```

4 仅将第n位置为1

```Python
x|(1<<n)
```

5 仅将第n位置为0

```Python
x&(~(1<<n))
```

6 将x最高位值第n位（含）清零

```Python
x&((1<<n)-1)
```

## 14.4 常用位运算

1 判断奇数偶数

```Python
x%2 == 1  =>  (x&1) == 1  
x%2 == 0  =>  (x&1) == 0
```

2 整除

```python
x // 2  =>  x >> 1 #右移一位
#例如
mid = (left + right) // 2 => mid = (left + right) >> 1
```

3 清零最低位的1

```python
x = x & (x-1)
```

4 得到最低位的1

```python
x & -x
```

5 

```python
x & -x => 0
```

# 17 布隆过滤器（bloom filter）和LRU cache

## 17.1 布隆过滤器

1 和字典相比，它只能用于检索一个元素是否在一个集合中，不能存储额外的信息。

2 优点：时间效率和空间效率远远超过一般算法

3 缺点：有一定的误识别率和删除困难（模糊查询）

4 布隆过滤器说有，不一定有。说没有，肯定没有。

5 一般当快速地缓存使用，例如查询数据库之前使用，先判断数据库中是否有，有再去数据库查，没有的话就不去数据库查询了，节省时间。

6 Python的hash函数有：

```python
# 10000000次
# 1 1.34 s
hash("123456") # 4571419676222125886
# 2 2.73 s
import mmh3
random_seed = 7
mmh3.hash("123456", random_seed) # 1203136047
# 3
s = "123456".encode()
import hashlib
# 3.1 2.07 s
hh1 = hashlib.md5()
hh1.update(s)
hh1.digest() # b'\xe1\n\xdc9I\xbaY\xab\xbeV\xe0W\xf2\x0f\x88>'
hh1.digest_size # 16
# 3.2 2.13 s
hh2 = hashlib.sha1()
hh2.update(s)
hh2.digest() # b'|J\x8d\t\xca7b\xafa\xe5\x95 \x94=\xc2d\x94\xf8\x94\x1b'
hh2.digest_size # 20
# 3.3 2.32 s
hh3 = hashlib.sha256()
hh3.update(s)
hh3.digest() # b'\x8d\x96\x9e\xefn\xca\xd3\xc2\x9a:b\x92\x80\xe6\x86\xcf\x0c?]Z\x86\xaf\xf3\xca\x12\x02\x0c\x92:\xdcl\x92'
hh3.digest_size # 32
# 3.4 1.8 s
hh4 = hashlib.sha3_256()
hh4.update(s)
hh4.digest() #b'\xd7\x19\x0e\xb1\x94\xff\x94\x94bU\x14\xb6\xd1x\xc8\x7f\x99\xc5\x97>(\xc3\x98\x96\x9d"3\xf2\x96\nW>'
hh4.digest_size #32

# 3.5 2.25 s
hh5 = hashlib.sha512()
hh5.update(s)
hh5.digest() # b'\xba2S\x87j\xedk\xc2-Jo\xf5=\x84\x06\xc6\xad\x86A\x95\xed\x14J\xb5\xc8v!\xb6\xc23\xb5H\xba\xea\xe6\x95m\xf3F\xec\x8c\x17\xf5\xea\x10\xf3^\xe3\xcb\xc5\x14y~\xd7\xdd\xd3\x14Td\xe2\xa0\xba\xb4\x13'
hh5.digest_size # 64
# 4 
import base64
# 4.1 3.94 s
base64.b16encode(s) # b'313233343536'
# 4.2 36.3 s
base64.b32encode(s) # b'GEZDGNBVGY======'
```

7 代码实现

```python
# Python 
from bitarray import bitarray 
import mmh3 
class BloomFilter: 
	def __init__(self, size, hash_num): 
		self.size = size 
		self.hash_num = hash_num 
		self.bit_array = bitarray(size) 
		self.bit_array.setall(0) 
	def add(self, s): 
		for seed in range(self.hash_num): 
			result = mmh3.hash(s, seed) % self.size 
			self.bit_array[result] = 1 
	def lookup(self, s): 
		for seed in range(self.hash_num): 
			result = mmh3.hash(s, seed) % self.size 
			if self.bit_array[result] == 0: 
				return "Nope" 
		return "Probably" 
bf = BloomFilter(500000, 7) 
bf.add("dantezhao") 
print (bf.lookup("dantezhao")) 
print (bf.lookup("yyj")) 
```

```java
//Java
public class BloomFilter {
    private static final int DEFAULT_SIZE = 2 << 24;
    private static final int[] seeds = new int[] { 5, 7, 11, 13, 31, 37, 61 };
    private BitSet bits = new BitSet(DEFAULT_SIZE);
    private SimpleHash[] func = new SimpleHash[seeds.length];
    public BloomFilter() {
        for (int i = 0; i < seeds.length; i++) {
            func[i] = new SimpleHash(DEFAULT_SIZE, seeds[i]);
        }
    }
    public void add(String value) {
        for (SimpleHash f : func) {
            bits.set(f.hash(value), true);
        }
    }
    public boolean contains(String value) {
        if (value == null) {
            return false;
        }
        boolean ret = true;
        for (SimpleHash f : func) {
            ret = ret && bits.get(f.hash(value));
        }
        return ret;
    }
    // 内部类，simpleHash
    public static class SimpleHash {
        private int cap;
        private int seed;
        public SimpleHash(int cap, int seed) {
            this.cap = cap;
            this.seed = seed;
        }
        public int hash(String value) {
            int result = 0;
            int len = value.length();
            for (int i = 0; i < len; i++) {
                result = seed * result + value.charAt(i);
            }
            return (cap - 1) & result;
        }
    }
}
```

## 17.2 LRU cache

LRU：最近最少使用 

1 python

```python
# Python 
class LRUCache(object): 
	def __init__(self, capacity): 
		self.dic = collections.OrderedDict() 
		self.remain = capacity
	def get(self, key): 
		if key not in self.dic: 
			return -1 
		v = self.dic.pop(key) 
		self.dic[key] = v   # key as the newest one 
		return v 
	def put(self, key, value): 
		if key in self.dic: 
			self.dic.pop(key) 
		else: 
			if self.remain > 0: 
				self.remain -= 1 
			else:   # self.dic is full
				self.dic.popitem(last=False) 
		self.dic[key] = value
```

2 c++

```c++
//C/C++

struct CacheNode {
    int key, value;
    CacheNode *pre, *next;
      
    CacheNode(int key_ = 0, int value_ = 0) 
        : key(key_), value(value_), pre(NULL), next(NULL) {}
};

class LRUCache {
public:
    LRUCache(int capacity) 
        : _capacity(capacity), _head(new CacheNode()), _tail(_head) {}
    
    int get(int key) {
        auto it = _cache.find(key);
        if (it == _cache.end()) return -1;
        
        moveToTail(it->second);
        return it->second->value;
    }
    
    void put(int key, int value) {
        auto it = _cache.find(key);
        
        if (it != _cache.end()) {
            it->second->value = value;
            moveToTail(it->second);
        }
        else if ((int)_cache.size() < _capacity) {
            auto node = new CacheNode(key, value);
            addToTail(node);          
            _cache[key] = node;
        }
        else {
            // Reuse existing node
            _cache.erase(_head->next->key);
            moveToTail(_head->next);
            _tail->key = key; _tail->value = value;
            _cache[key] = _tail;
        }
    }
    
    ~LRUCache() {
        auto pCurr = _head;
        while (pCurr != NULL) {
            auto next = pCurr->next;
            delete pCurr;
            pCurr = next;
        }
    }
    
private:
    const int _capacity;
    CacheNode *const _head, *_tail;
    unordered_map<int, CacheNode*> _cache;
    
    void moveToTail(CacheNode *node) {
        if (node == _tail) return;
        
        node->pre->next = node->next;
        node->next->pre = node->pre;
        
        addToTail(node);
    }
    
    void addToTail(CacheNode *node) {
        node->next = _tail->next;
        _tail->next = node;
        node->pre = _tail;
        _tail = node;                   
    }
};
```

3 java

```java
/**
 * 使用 哈希表 + 双端链表 实现
 */
class LinkedNode {
  constructor(key = 0, val = 0) {
    this.key = key
    this.val = val
    this.prev = null
    this.next = null
  }
}


class LinkedList {
  constructor() {
    this.head = new LinkedNode()
    this.tail = new LinkedNode()
    this.head.next = this.tail
    this.tail.prev = this.head
  }


  insertFirst(node) {
    node.next = this.head.next
    node.prev = this.head
    this.head.next.prev = node
    this.head.next = node
  }


  remove(node) {
    node.prev.next = node.next
    node.next.prev = node.prev
  }


  removeLast() {
    if (this.tail.prev === this.head) return null
    let last = this.tail.prev
    this.remove(last)
    return last
  }
}


/**
 * @param {number} capacity
 */
var LRUCache = function(capacity) {
  this.capacity = capacity
  this.keyNodeMap = new Map()
  this.cacheLink = new LinkedList()
};


/** 
 * @param {number} key
 * @return {number}
 */
LRUCache.prototype.get = function(key) {
  if (!this.keyNodeMap.has(key)) return -1
  let val = this.keyNodeMap.get(key).val
  this.put(key, val)
  return val
};


/** 
 * @param {number} key 
 * @param {number} value
 * @return {void}
 */
LRUCache.prototype.put = function(key, value) {
  let size = this.keyNodeMap.size
  if (this.keyNodeMap.has(key)) {
    this.cacheLink.remove(this.keyNodeMap.get(key)); 
    --size 
  }
  if (size >= this.capacity) {
    this.keyNodeMap.delete(this.cacheLink.removeLast().key)
  }
  let node = new LinkedNode(key, value)
  this.keyNodeMap.set(key, node)
  this.cacheLink.insertFirst(node)
};
```

```java
class LRUCache {
    /**
     * 缓存映射表
     */
    private Map<Integer, DLinkNode> cache = new HashMap<>();
    /**
     * 缓存大小
     */
    private int size;
    /**
     * 缓存容量
     */
    private int capacity;
    /**
     * 链表头部和尾部
     */
    private DLinkNode head, tail;

    public LRUCache(int capacity) {
        //初始化缓存大小，容量和头尾节点
        this.size = 0;
        this.capacity = capacity;
        head = new DLinkNode();
        tail = new DLinkNode();
        head.next = tail;
        tail.prev = head;
    }

    /**
     * 获取节点
     * @param key 节点的键
     * @return 返回节点的值
     */
    public int get(int key) {
        DLinkNode node = cache.get(key);
        if (node == null) {
            return -1;
        }
        //移动到链表头部
         (node);
        return node.value;
    }

    /**
     * 添加节点
     * @param key 节点的键
     * @param value 节点的值
     */
    public void put(int key, int value) {
        DLinkNode node = cache.get(key);
        if (node == null) {
            DLinkNode newNode = new DLinkNode(key, value);
            cache.put(key, newNode);
            //添加到链表头部
            addToHead(newNode);
            ++size;
            //如果缓存已满，需要清理尾部节点
            if (size > capacity) {
                DLinkNode tail = removeTail();
                cache.remove(tail.key);
                --size;
            }
        } else {
            node.value = value;
            //移动到链表头部
            moveToHead(node);
        }
    }

    /**
     * 删除尾结点
     *
     * @return 返回删除的节点
     */
    private DLinkNode removeTail() {
        DLinkNode node = tail.prev;
        removeNode(node);
        return node;
    }

    /**
     * 删除节点
     * @param node 需要删除的节点
     */
    private void removeNode(DLinkNode node) {
        node.next.prev = node.prev;
        node.prev.next = node.next;
    }

    /**
     * 把节点添加到链表头部
     *
     * @param node 要添加的节点
     */
    private void addToHead(DLinkNode node) {
        node.prev = head;
        node.next = head.next;
        head.next.prev = node;
        head.next = node;
    }

    /**
     * 把节点移动到头部
     * @param node 需要移动的节点
     */
    private void moveToHead(DLinkNode node) {
        removeNode(node);
        addToHead(node);
    }

    /**
     * 链表节点类
     */
    private static class DLinkNode {
        Integer key;
        Integer value;
        DLinkNode prev;
        DLinkNode next;

        DLinkNode() {
        }

        DLinkNode(Integer key, Integer value) {
            this.key = key;
            this.value = value;
        }
    }
}
```

# 18 排序算法

1比较类排序：通过比较来决定元素间相对次序，时间复杂度不能突破nlogn, 成为非线性时间排序。（可以是对象排序，不仅仅是数字排序）

2 非比较类排序：不通过比较来决定元素间相对次序，可以线性时间运行，以此也成为了线性时间非比较类排序。（一般仅仅是数字排序）

3 

![](E:\my_note\09_geek\my_note\note_images\2.png)

## 18.1 普通排序

时间复杂度：$O(n^2)$

### 18.1.1  选择排序 Selection Sort

```Python
# 1
def selection_sort(nums):
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                
# 2
def selection_sort2(nums):
    for i in range(len(nums)-1):
        min_val = nums[i]
        min_val_index = i
        for j in range(i+1, len(nums)):
            if nums[j] < min_val:
                min_val = nums[j]
                min_val_index = j
        nums[i], nums[min_val_index] = nums[min_val_index], nums[i]
        
selection_sort(nums)
```

### 18.1.2 插入排序 Insertion Sort

```python
# 1
def insertion_sort(nums):
    for i in range(1, len(nums)):
        j = i - 1
        while j > 0 and nums[i] < nums[j]:
            j -= 1
        nums.insert(j+1, nums.pop(i))
        
# 2
def insertion_sort2(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and key < nums[j]:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = key
```

### 18.1.3 冒泡排序 Bubble Sort

```python
# 1
def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(len(nums)-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                
# 2
def bubble_sort2(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums)-1-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
```



## 18.2 高级排序

时间复杂度$O(nlogn)$

### 18.2.1 快排

分治的思想

O（nlogn）：主定理可以推出时间复杂度

**1 最好的情况下：**
$$
T(n) = O(n) + 2T(\frac{n}{2})\\
= O(n) + 2 *[O(\frac{n}{2}) + 2*T(\frac{n}{4})]\\
=...\\
=O(n) + O(n) +...+ O(n)\\
=0(nlogn)
$$
推出O（nlogn）

**2 最坏的情况下（逆序）:**
$$
T(n) = O(n) + T(n-1)\\
= O(n) + O(n-1) + T(n-2)\\
= ...\\
= O(n) + O(n-1) + ... + O(1)
= O(n^2)
$$
推出O（n^2）

3 **快排优化**：

​	可以随机打乱一下，这样，即使逆序也变得杂乱。

​	或者随机中间值 作为哨兵而不是选择第一个值或最后一个值作为哨兵。

**4 模板**

```python
#Python
def quick_sort(begin, end, nums):
    if begin >= end:
        return
    pivot_index = partition(begin, end, nums)
    quick_sort(begin, pivot_index-1, nums)
    quick_sort(pivot_index+1, end, nums)
    
def partition(begin, end, nums):
    pivot = nums[begin]
    mark = begin
    for i in range(begin+1, end+1):
        if nums[i] < pivot:
            mark +=1
            nums[mark], nums[i] = nums[i], nums[mark]
    nums[begin], nums[mark] = nums[mark], nums[begin]
    return mark

# 调用方式
quick_sort(0, len(nums)-1, nums)
```

### 18.2.2 归并排序（merge sort）

分治思想

```python
def merge_sort(array, left, right):
    if left >= right:
        return
    mid = (left + right) >> 1 # mid = (left + right) // 2
    merge_sort(array, left, mid)
    merge_sort(array, mid+1, right)
    merge(array, left, mid, right)


def merge(array, left, mid, right):
    temp = []
    i, j = left, mid + 1
    while i <= mid and j <= right:
        if array[i] <= array[j]:
            temp.append(array[i])
            i += 1
        else:
            temp.append(array[j])
            j += 1
         
    if i <= mid:
        temp += array[i:mid + 1]
    else:
        temp += array[j:right + 1]
    array[left:right + 1] = temp
```

```python
def mergesort(seq):
    """归并排序"""
    if len(seq) <= 1:
        return seq
    mid = len(seq) // 2  # 将列表分成更小的两个列表
    # 分别对左右两个列表进行处理，分别返回两个排序好的列表
    left = mergesort(seq[:mid])
    right = mergesort(seq[mid:])
    # 对排序好的两个列表合并，产生一个新的排序好的列表
    return merge(left, right)

def merge(left, right):
    """合并两个已排序好的列表，产生一个新的已排序好的列表"""
    result = []  # 新的已排序好的列表
    i = 0  # 下标
    j = 0
    # 对两个列表中的元素 两两对比。
    # 将最小的元素，放到result中，并对当前列表下标加1
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

seq = [5,3,0,6,1,4]
print '排序前：',seq
result = mergesort(seq)
print '排序后：',result
```

### 18.2.3 堆排序 Heap Sort

堆插入O（logn）,取最小值或最大值O(1)

1 数组元素依次插入建立小顶堆

2 依次取出堆顶元素并删除

```python
import heapq
def heap_sort(array):
    pq = []
    n = len(array)
    for i in range(n):
        heapq.heappush(pq, array[i])
    for i in range(n):
        array[i] = heapq.heappop(pq)
```

```python
# 更快，线性时间
import heapq
def heap_sort(array):
    pq = array.copy()
    heapq.heapify(pq)
    for i in range(len(array)):
        array[i] = heapq.heappop(pq)
```

```python
#Python
def heapify(parent_index, length, nums):
    temp = nums[parent_index]
    child_index = 2*parent_index+1
    while child_index < length:
        if child_index+1 < length and nums[child_index+1] > nums[child_index]:
            child_index = child_index+1
        if temp > nums[child_index]:
            break
        nums[parent_index] = nums[child_index]
        parent_index = child_index
        child_index = 2*parent_index + 1
    nums[parent_index] = temp

def heapsort(nums):
    for i in range((len(nums)-2)//2, -1, -1):
        heapify(i, len(nums), nums)
    for j in range(len(nums)-1, 0, -1):
        nums[j], nums[0] = nums[0], nums[j]
        heapify(0, j, nums)
```

## 18.3 特殊排序

时间复杂度: $O(n)$

特殊排序不是重点

### 18.3.1 计数排序

1元素必须是整数

2 元素值不能太大

### 18.3.2 桶排序

计数排序的升级版

### 18.3.3 基数排序

 只能排整型数

# 19 高级动态规划

## 19.1 复习

### 19.1.1 递归

函数自己调用自己

```python
def recursion(level, param1, param2, ...): 
    # recursion terminator 1 递归终止条件
    if level > MAX_LEVEL: 
	   process_result 
	   return 
    # process logic in current level 2 处理本层逻辑
    process(level, data...) 
    # drill down 3 下到下一层
    self.recursion(level + 1, p1, ...) 
    # reverse the current level status if needed 4 如果需要的话，清除本层的变量
```

### 19.1.2 分治

分而治之（例如归并排序）

```Python
![3](E:\my_note\09_geek\my_note\note_images\3.png)# Python
def divide_conquer(problem, param1, param2, ...): 
  # recursion terminator 1 递归终止条件
  if problem is None: 
	print_result 
	return 
  # prepare data 2 准备数据和拆分问题
  data = prepare_data(problem) 
  subproblems = split_problem(problem, data) 
  # conquer subproblems 3 对子问题调分治函数递归求解
  subresult1 = self.divide_conquer(subproblems[0], p1, ...) 
  subresult2 = self.divide_conquer(subproblems[1], p1, ...) 
  subresult3 = self.divide_conquer(subproblems[2], p1, ...) 
  …
  # process and generate the final result 4 合并结果
  result = process_result(subresult1, subresult2, subresult3, …)
	
  # revert the current level states 5 清除本层状态变量
```

![](E:\my_note\09_geek\my_note\note_images\3.png)

### 19.1.3 回溯

### 19.1.4 动态规划

分治+最优子结构+动态递推

动态规划和递归或者分治没有根本的区别（关键看有无最优子结构)

共性：都是找到重复子问题

差异性：动态规划是找到最优子结构，中途可以淘汰次优解

难点：状态转移方程

例如：

​	1 斐波那契数列：f(n) = f(n-1) + f(n-2)

​	2 路径问题：f(x,y) = f(x-1, y) + f(x, y-1)

​	3 

## 19.2 思维

1 人肉递归低效，很累

2 找到最近最简方法，将其拆解成可重复性解决的问题

3 数学归纳法的思维

## 19.3 复杂的原因

1 状态的维度更多了（二维，三维，或更多，甚至需要压缩）

2 状态方程更加复杂

## 19.4 进阶版爬楼梯

**1 若每次能走1，2，3，则结果？（easy）**

```python
# 1.1
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n <= 2:
#             return n
#         if n == 3:
#             return 4
#         f1, f2, f3 = 1, 2, 4
#         for i in range(4, n+1):
#             f = f1 + f2 + f3
#             f1, f2, f3 = f2, f3, f
#         return f3

# 1.2 7040ms
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         def helper(n):
#             if n <= 2:
#                 return n
#             if n == 3:
#                 return 4
#             return helper(n-1) + helper(n-2) + helper(n-3)
#         return helper(n)

# 1.3 0ms
# from functools import lru_cache
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         @lru_cache(None)
#         def helper(n):
#             if n <= 2:
#                 return n
#             if n == 3:
#                 return 4
#             return helper(n-1) + helper(n-2) + helper(n-3)
#         return helper(n)
#
# print(Solution().climbStairs(1))
# print(Solution().climbStairs(2))
# print(Solution().climbStairs(3))
# print(Solution().climbStairs(4))
# print(Solution().climbStairs(5))
# print(Solution().climbStairs(30))
# 1， 2， 4， 7， 13， 53798080
```

**2 若每次步长为steps里，则结果？（类似硬518. 零钱兑换 II）**

```python
# 2.1
# DP
# from typing import List
# class Solution:
#     def climbStairs(self, amount: int, coins: List[int]) -> int:
#         dp = [0] * (amount+1)
#         dp[0] = 1
#         for i in range(1, amount+1):
#             for c in coins:
#                 if i - c >= 0:
#                     dp[i] += dp[i - c]
#         return dp[-1]

# 2.2
# 递归
# from typing import List
# from functools import lru_cache
# class Solution:
#     def climbStairs(self, amount: int, coins: List[int]) -> int:
#         @lru_cache(None)
#         def helper(n):
#             if n < 0:
#                 return 0
#             if n == 0:
#                 return 1
#             return sum(helper(n-c) for c in coins)
#
#         return helper(amount)

# print(Solution().climbStairs(1, [1,2,3]))
# print(Solution().climbStairs(2, [1,2,3]))
# print(Solution().climbStairs(3, [1,2,3]))
# print(Solution().climbStairs(4, [1,2,3]))
# print(Solution().climbStairs(5, [1,2,3]))
# print(Solution().climbStairs(30, [1,2,3]))
# print(Solution().climbStairs(30, [1,2,5]))
# 1， 2， 4， 7， 13， 53798080, 5508222
```

**3 若相邻两步的步伐不能一样，则结果如何？（mid）**

```python
# 3 dp
# class Solution:
#     def climbStairs(self, amount: int, steps: List[int]) -> int:
#         dp = [[0]*len(steps) for _ in range(amount+1)]
#         for i in range(1, amount+1):
#             for j in range(len(steps)):
#                 if i == steps[j]:
#                     dp[i][j] = 1
#                 elif i - steps[j] > 0:
#                     for k in range(len(steps)):
#                         if k != j:
#                             dp[i][j] += dp[i - steps[j]][k]
#         return sum(dp[-1])

# 循环
# dp[i][j]表示走到i步，且到这步走了steps[j]步
# 那么dp[i][j] = sum(dp[i - steps[j]][k]) k != j
# 起始条件是
# dp[steps[j]][j] = 1, j从0到ns - 1
# dp[负数][j] = 0
# class Solution:
#     def climbStairs(self, n: int, steps: List[int]) -> int:
#         ns = len(steps)
#         dp = [[0 for _ in range(ns)] for _ in range(n + 1)]
#
#         for i in range(n + 1):
#             for j in range(ns):
#                 if i == steps[j]:
#                     dp[i][j] = 1
#                 else:
#                     res = 0
#                     for k in range(ns):
#                         if k != j and i >= steps[j]:
#                             res += dp[i - steps[j]][k]
#                     dp[i][j] = res
#                     # dp[i][j] = sum(dp[i - steps[j]][k] for k in range(ns) if k != j and i >= steps[j])
#         return sum(dp[n])

# print(Solution().climbStairs(1, [1,2,3]))
# print(Solution().climbStairs(2, [1,2,3]))
# print(Solution().climbStairs(3, [1,2,3]))
# print(Solution().climbStairs(4, [1,2,3]))
# print(Solution().climbStairs(5, [1,2,3]))
# print(Solution().climbStairs(30, [1,2,3]))
# print(Solution().climbStairs(30, [1,2,5]))
# # 1, 1, 3, 3, 4, 32103, 2487
```

**4 输出所有的路径结果**

dfs

# 20 字符串算法

## 20.1 字符串immutable

Python中的字段串是不可变（immutable）类型

## 20.2 atoi模板

(表示ascii to integer)是把字符串转换成整型数的一个函数

```Python
# Python
class Solution(object):
    def myAtoi(self, s):
        if len(s) == 0 : return 0
        ls = list(s.strip())
        
        sign = -1 if ls[0] == '-' else 1
        if ls[0] in ['-','+'] : del ls[0]
        ret, i = 0, 0
        while i < len(ls) and ls[i].isdigit() :
            ret = ret*10 + ord(ls[i]) - ord('0')
            i += 1
        return max(-2**31, min(sign * ret,2**31-1))
```

## 20.3 常见字符串题目

经常字符串和动态规划相结合

**最长子串，子序列问题**

子序列可以有间隔，子串不能有间隔

1 最长子序列（NO.1143）

```python
if text1[i - 1] == text2[j - 1]:  # 不是 text1[i] == text2[j]
    dp[i][j] = dp[i - 1][j - 1] + 1
else:
    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
return dp[-1][-1]
```

2 最长子串

```python
if text1[i - 1] == text2[j - 1]:  # 不是 text1[i] == text2[j]
    dp[i][j] = dp[i - 1][j - 1] + 1
else:
    dp[i][j] = 0
# 最后再所有的值中找最大值，而不是最后的值
```

3 编辑距离（NO.72）

```python
if text1[i - 1] == text2[j - 1]: 
    dp[i][j] = dp[i - 1][j - 1]
else:
    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j])
return dp[-1][-1]
```

4 最长回文子串（NO.5）

```python
# P(i, j)代表s[i:j+1]是不是回文串（注意，i，j都是索引）
#if s[i] == s[j] and dp[i+1][j-1]:
if s[i] == s[j] and (j - i <= 1 or dp[i+1][j-1]):
    dp[i][j] = True
else:
    dp[i][j] = False
```

5 通配符匹配问题（NO.10）

​	加缓存memo

```python
pre = bool(s) and p[0] in {s[0], "."}
if len(p) >= 2 and p[1] == "*":
    return self.isMatch(s, p[2:]) or (pre and self.isMatch(s[1:], p)) # * 匹配0次或多次
else:
    return pre and self.isMatch(s[1:], p[1:])
```

```python
pre = i < len_s and p[j] in {s[i], "."}
if j + 1 <= len_p - 1 and p[j + 1] == "*":
    ans = dp(i, j + 2) or (pre and dp(i + 1, j))
else:
    ans = pre and dp(i + 1, j + 1)
memo[(i, j)] = ans
```

```python
# 斐波那契数列和本问题的对比
def fib(n):
    fib(n - 1) #1
    fib(n - 2) #2
    
def dp(i, j):
    dp(i, j + 2)     #1 * 匹配0次
    dp(i + 1, j)     #2 * 匹配1次
    dp(i + 1, j + 1) #3 没有*
```

6 不同的子序列(NO.115)

```python
# s是原料，可以不用完，t是目标，必须达成
#dp[i][j]代表t[:i]能用s[:j]来组成的个数
if t[i - 1] == s[j - 1]:
    dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
else:
    dp[i][j] = dp[i][j - 1]
return dp[-1][-1] 
```

## 20.4 字符串匹配算法

### 1 暴力法（brute force）

O（mn）,m和n分别为两个字符串的长度

```python
def force_search(txt, pat):
    m, n = len(txt), len(pat)
    for i in range(m-n):
        for j in range(n):
            if txt[i+j] != pat[j]:
                break
        else:
            return i
    return -1

print(force_search("BBC ABCDAB ABCDABCDABDE", "ABCDABD"))
```

### 2 rabin-karp算法

比较txt[i:i+n]的哈希值与pat的哈希值是否相等，如果相等再暴力一个一个字母比较，如果不等直接i加1

```python
# O(mn)
def rabin_karp_search(txt, pat):
    m, n = len(txt), len(pat)
    hash_pat = hash(pat)
    for i in range(m-n):
        if hash(txt[i:i+n]) != hash_pat:
            continue
        for j in range(n):
            if txt[i+j] != pat[j]:
                break
        else:
            return i
    return -1

# def rabin_karp_search(txt, pat):
#     m, n = len(txt), len(pat)
#     set_pat = set(pat)
#     for i in range(m-n):
#         if set(txt[i:i+n]) != set_pat:
#             continue
#         for j in range(n):
#             if txt[i+j] != pat[j]:
#                 break
#         else:
#             return i
#     return -1
```

通过滑动窗口来加速

O(m)

```python
# 老师给的
#Python
class Solution:
    def strStr(self, txt: str, pat: str) -> int:
        M, N = len(txt), len(pat)
        if N > M:
            return -1

        Q = 9997 # 是素数就行,例如99197
        higest_pow = pow(256, N-1) % Q # 最高位权重
        txt_hash = pat_hash = 0
        for i in range(N): # preprocessing
            txt_hash = (256 * txt_hash + ord(pat[i])) % Q
            pat_hash = (256 * pat_hash + ord(txt[i])) % Q
        for i in range(M-N+1): # note the +1
            if txt_hash == pat_hash: # check character by character
                for j in range(N):
                    if pat[j] != txt[i + j]:
                        break
                else:
                    return i
            if i < M-N:
                pat_hash = (pat_hash - higest_pow * ord(txt[i])) % Q
                pat_hash = (pat_hash * 256 + ord(txt[i + N])) % Q
                pat_hash = (pat_hash + Q) % Q # 防止出现负数（例如-3%7）
        return -1
```

### 3 KMP算法

 找已经匹配的地方的最前面和最后索引，下次直接移到下一个

```python

```

### 4 Boyer-Moore算法

### 5 sunday算法

# 21 复习

![](E:\my_note\09_geek\my_note\note_images\4.png)

onenote

notes

xmind

mindnote