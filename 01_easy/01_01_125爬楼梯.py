# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
#
#  说明：本题中，我们将空字符串定义为有效的回文串。
#
#  示例 1:
#
#  输入: "A man, a plan, a canal: Panama"
# 输出: true
#
#
#  示例 2:
#
#  输入: "race a car"
# 输出: false
#
#  Related Topics 双指针 字符串


# leetcode submit region begin(Prohibit modification and deletion)
# 1 解答成功: 执行耗时:40 ms,击败了98.10% 的Python3用户 内存消耗:14.5 MB,击败了11.11% 的Python3用户
# O(n), O(n)
import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        valida_str = string.digits + string.ascii_lowercase
        s = "".join([i for i in s.lower() if i in valida_str])
        return s == s[::-1]

# 2 解答成功: 执行耗时:44 ms,击败了94.95% 的Python3用户 内存消耗:14.4 MB,击败了37.04% 的Python3用户
# O(n), O(n)
#
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         s = "".join([i for i in s if i.isalnum()]).upper()
#         return s == s[::-1]
# 3 解答成功: 执行耗时:52 ms,击败了81.02% 的Python3用户 内存消耗:14.9 MB,击败了7.41% 的Python3用户
# O(n), O(n)
# import re
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         s = "".join(re.findall(r"[a-zA-Z0-9]+", s)).lower()
#         return s == s[::-1]
#
#
#
# 4 解答成功: 执行耗时:76 ms,击败了26.81% 的Python3用户 内存消耗:19.3 MB,击败了7.41% 的Python3用户
# O(n), O(n)
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         i = 0
#         L = []
#         while i < len(s):
#             if s[i].isalnum():
#                 L.append(s[i].lower())
#             i += 1
#         s = "".join(L)
#         return s == s[::-1]

# leetcode submit region end(Prohibit modification and deletion)
