# 给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
#
#  最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
#
#  你可以假设除了整数 0 之外，这个整数不会以零开头。
#
#  示例 1:
#
#  输入: [1,2,3]
# 输出: [1,2,4]
# 解释: 输入数组表示数字 123。
#
#
#  示例 2:
#
#  输入: [4,3,2,1]
# 输出: [4,3,2,2]
# 解释: 输入数组表示数字 4321。
#
#  Related Topics 数组


# leetcode submit region begin(Prohibit modification and deletion)
# 1 解答成功: 执行耗时:48 ms,击败了22.40% 的Python3用户 内存消耗:13.6 MB,击败了6.82% 的Python3用户
# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         num = int("".join(map(str, digits))) + 1
#         res = []
#         for i in range(len(str(num))-1, -1, -1):
#             n = num // 10**i
#             res.append(n)
#             num = num % 10**i
#         return res

# 2 解答成功: 执行耗时:44 ms,击败了43.95% 的Python3用户 内存消耗:13.6 MB,击败了6.82% 的Python3用户
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(-1, -len(digits) - 1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        else:
            digits.insert(0, 1)
        return digits

# leetcode submit region end(Prohibit modification and deletion)
