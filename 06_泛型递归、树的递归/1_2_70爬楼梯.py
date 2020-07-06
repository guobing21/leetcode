# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
#
#  每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
#
#  注意：给定 n 是一个正整数。
#
#  示例 1：
#
#  输入： 2
# 输出： 2
# 解释： 有两种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶
# 2.  2 阶
#
#  示例 2：
#
#  输入： 3
# 输出： 3
# 解释： 有三种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶 + 1 阶
# 2.  1 阶 + 2 阶
# 3.  2 阶 + 1 阶
#
#  Related Topics 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
# 1 解答成功: 执行耗时:28 ms,击败了98.47% 的Python3用户 内存消耗:13.7 MB,击败了20.59% 的Python3用户
# O(n), O(1)
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n <= 2:
#             return n
#         t1, t2 = 1, 2
#         for i in range(3, n+1):
#             t = t1 + t2
#             t1, t2 = t2, t
#         return t2

# 2 解答成功: 执行耗时:36 ms,击败了82.71% 的Python3用户 内存消耗:13.7 MB,击败了20.59% 的Python3用户
# O(n), O(n)

# class Solution:
#     caches = {}
#     def climbStairs(self, n: int) -> int:
#         if n <= 3:
#             return n
#         if n-1 in Solution.caches:
#             res01 = Solution.caches[n-1]
#         else:
#             res01 = self.climbStairs(n-1)
#             Solution.caches[n-1] = res01
#
#         if n-2 in Solution.caches:
#             res02 = Solution.caches[n-2]
#         else:
#             res02 = self.climbStairs(n-2)
#             Solution.caches[n-2] = res02
#
#         return res01 + res02

# 3 解答成功: 执行耗时:36 ms,击败了82.71% 的Python3用户 内存消耗:13.9 MB,击败了20.59% 的Python3用户
# O(n), O(n)
#
# from functools import lru_cache
# class Solution:
#     @lru_cache(maxsize=10000)
#     def climbStairs(self, n: int) -> int:
#         if n <= 3:
#             return n
#         return self.climbStairs(n-1) + self.climbStairs(n-2)

# 4 解答成功: 执行耗时:44 ms,击败了39.47% 的Python3用户 内存消耗:13.7 MB,击败了20.59% 的Python3用户
# O(n),O(n)
#
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n <= 2:
#             return n
#         steps = [1, 2]
#         while len(steps) < n:
#             steps.append(steps[-1] + steps[-2])
#         return steps[-1]

# 5 运行失败: Time Limit Exceeded stdout: null
# 不建议
# 时间O（2^n）,空间O（n）
#
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n <= 3:
#             return n
#         return self.climbStairs(n-1) + self.climbStairs(n-2)
# 6
# https://zhuanlan.zhihu.com/p/56444434
# F(1) = 1, F(2)= 2, F(3)= F(1)+F(2)= 3
# F(3) = F(2) + F(1)
# F(2) = F(2) + 0
#
# [F(3)]       [1, 1]     [F(2)]
#        =             *
# [F(2)]       [1, 0]     [F(1)]

#
# [F(n)]         [1, 1]^(n-2)     [F(2)]
#          =             *
# [F(n-1)]       [1, 0]     [F(1)]
# # 6.1 解答成功: 执行耗时:140 ms,击败了6.25% 的Python3用户 内存消耗:29 MB,击败了20.59% 的Python3用户
# import numpy as np
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n <= 2:
#             return n
#         res = np.mat([[1, 1], [1, 0]])**(n-2) * np.mat([[2], [1]])
#         return int(res[0, 0])

# 6.2 改进版 解答成功: 执行耗时:100 ms,击败了6.25% 的Python3用户 内存消耗:30.7 MB,击败了20.59% 的Python3用户
#A=S*l*SI
#A^2=S*l*SI * S*l*SI
import numpy as np
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        A = np.mat([[1, 1], [1, 0]])
        eigvalues, eigvects = np.linalg.eig(A)
        res = eigvects * np.diag(eigvalues)**(n-2) * eigvects.I * np.mat([[2], [1]])
        return int(round(res[0,0]))



# leetcode submit region end(Prohibit modification and deletion)
