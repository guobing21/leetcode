# 实现 pow(x, n) ，即计算 x 的 n 次幂函数。
#
#  示例 1:
#
#  输入: 2.00000, 10
# 输出: 1024.00000
#
#
#  示例 2:
#
#  输入: 2.10000, 3
# 输出: 9.26100
#
#
#  示例 3:
#
#  输入: 2.00000, -2
# 输出: 0.25000
# 解释: 2-2 = 1/22 = 1/4 = 0.25
#
#  说明:
#
#
#  -100.0 < x < 100.0
#  n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。
#
#  Related Topics 数学 二分查找


# leetcode submit region begin(Prohibit modification and deletion)
# 1 运行失败: Time Limit Exceeded stdout: null
# O(n),O(1)
# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         result = 1
#         if n == 0:
#             return result
#         elif n > 0:
#             for i in range(n):
#                 result *= x
#         else:
#             for i in range(-n):
#                 result *= x
#             result = 1 / result
#         return result

# 2 解答成功: 执行耗时:40 ms,击败了74.95% 的Python3用户 内存消耗:13.7 MB,击败了8.33% 的Python3用户
# 分治
# 时间复杂度：O(logn)，即为递归的层数。
# 空间复杂度：O(logn)，即为递归的层数。这是由于递归的函数调用会使用栈空间。
# 准确来说是log以2为底的
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(n):
            if n == 0:
                return 1.0
            y = helper(n//2)
            return y * y if n % 2 == 0 else y * y * x
        return helper(n) if n >= 0 else 1.0 / helper(-n)


# leetcode submit region end(Prohibit modification and deletion)
