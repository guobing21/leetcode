# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
#
#  示例 1:
#
#  输入: s = "anagram", t = "nagaram"
# 输出: true
#
#
#  示例 2:
#
#  输入: s = "rat", t = "car"
# 输出: false
#
#  说明:
# 你可以假设字符串只包含小写字母。
#
#  进阶:
# 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
#  Related Topics 排序 哈希表


# leetcode submit region begin(Prohibit modification and deletion)
# 1 解答成功: 执行耗时:60 ms,击败了69.76% 的Python3用户 内存消耗:13.9 MB,击败了8.33% 的Python3用户
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         dict1, dict2 = {}, {}
#         for i in s:
#             if i not in dict1:
#                 dict1[i] = 1
#             else:
#                 dict1[i] += 1
#         for i in t:
#             if i not in dict2:
#                 dict2[i] = 1
#             else:
#                 dict2[i] += 1
#         return dict1 == dict2

# from collections import Counter
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         s_list = list(s)
#         t_list = list(t)
#         conter1 = Counter(s_list)
#         conter2 = Counter(t_list)
#         return conter1 == conter2

# from collections import Counter
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         conter1 = Counter(s)
#         conter2 = Counter(t)
#         return conter1 == conter2

# 2 解答成功: 执行耗时:56 ms,击败了78.25% 的Python3用户 内存消耗:13.8 MB,击败了8.33% 的Python3用户
# from collections import defaultdict
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         dict1, dict2 = defaultdict(int), defaultdict(int)
#         for i in s:
#             dict1[i] += 1
#         for i in t:
#             dict2[i] += 1
#         return dict1 == dict2
#

# # 3 解答成功: 执行耗时:60 ms,击败了69.76% 的Python3用户 内存消耗:14.7 MB,击败了8.33% 的Python3用
# # O(NlogN)
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         l1, l2 = sorted(s), sorted(t)
#         return l1 == l2

# 4 解答成功: 执行耗时:40 ms,击败了98.52% 的Python3用户 内存消耗:13.8 MB,击败了8.33% 的Python3用户
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
#         else:
#             set_s, set_t = set(s), set(t)
#             if set_s != set_t:
#                 return False
#             else:
#                 for i in set_s:
#                     if s.count(i) != t.count(i):
#                         return False
#         return True
# 5 解答成功: 执行耗时:64 ms,击败了57.31% 的Python3用户 内存消耗:13.6 MB,击败了12.50% 的Python3用户
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return abs(sum(ord(i)**0.5 for i in s) - sum(ord(i)**0.5 for i in t)) < 1e-5

# leetcode submit region end(Prohibit modification and deletion)
