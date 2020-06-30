# 编写一个程序，找出第 n 个丑数。
#
#  丑数就是质因数只包含 2, 3, 5 的正整数。
#
#  示例:
#
#  输入: n = 10
# 输出: 12
# 解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
#
#  说明:
#
#
#  1 是丑数。
#  n 不超过1690。
#
#  Related Topics 堆 数学 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
# 1 解答成功: 执行耗时:1108 ms,击败了6.24% 的Python3用户 内存消耗:13.9 MB,击败了12.50% 的Python3用户
from queue import PriorityQueue
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        pq = PriorityQueue()
        res = set()

        pq.put(1)
        res.add(1)

        i = 1
        while True:
            num = pq.get()
            if i == n:
                return num
            i += 1
            for new_num in num * 2, num * 3, num * 5:
                if new_num not in res:
                    res.add(new_num)
                    pq.put(new_num)
# 2
# 运行失败: Time Limit Exceeded stdout: null
# class Solution:
#     def is_ugly_num(self, num):
#         while True:
#             if num == 1:
#                 return True
#             elif num % 2 == 0:
#                 num = num/2
#             elif num % 3 == 0:
#                 num = num/3
#             elif num % 5 == 0:
#                 num = num/5
#             else:
#                 return False
#
#     def nthUglyNumber(self, n: int) -> int:
#         count = 0
#         i = 1
#         while True:
#             if self.is_ugly_num(i):
#                 count += 1
#             if count == n:
#                 return i
#             i += 1

# class Solution:
#     def __init__(self):
#         self.ugly_num = set([1])
#         self.no_ugly_num = set()
#     def is_ugly_num(self, num):
#         num_copy = num
#         while True:
#             if num in self.ugly_num:
#                 self.ugly_num.add(num_copy)
#                 return True
#             if num in self.no_ugly_num:
#                 self.no_ugly_num.add(num_copy)
#                 return False
#
#             if num % 2 == 0:
#                 num = num/2
#             elif num % 3 == 0:
#                 num = num/3
#             elif num % 5 == 0:
#                 num = num/5
#             else:
#                 self.no_ugly_num.add(num_copy)
#                 return False
#
#     def nthUglyNumber(self, n: int) -> int:
#         count = 0
#         i = 1
#         while True:
#             if self.is_ugly_num(i):
#                 count += 1
#             if count == n:
#                 return i
#             i += 1
# leetcode submit region end(Prohibit modification and deletion)
