# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
#
#  给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
#
#
#
#  示例:
#
#  输入："23"
# 输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
#
#
#  说明:
# 尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。
#  Related Topics 字符串 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
# 1 解答成功: 执行耗时:36 ms,击败了85.67% 的Python3用户 内存消耗:13.8 MB,击败了5.41% 的Python3用户
# class Solution:
#     def letterCombinations(self, digits: str) -> List[str]:
#         cp = {
#             "2": ["a", "b", "c"],
#             "3": ["d", "e", "f"],
#             "4": ["g", "h", "i"],
#             "5": ["j", "k", "l"],
#             "6": ["m", "n", "o"],
#             "7": ["p", "q", "r", "s"],
#             "8": ["t", "u", "v"],
#             "9": ["w", "x", "y", "z"]
#         }
#         res = []
#         n = len(digits)
#         if n == 0:
#             return res
#
#         def helper(s):
#             if len(s) == n:
#                 res.append(s)
#                 return
#             for i in cp[digits[len(s)]]:
#                 helper(s + i)
#
#         helper("")
#         return res

# 2 解答成功: 执行耗时:36 ms,击败了85.67% 的Python3用户 内存消耗:13.7 MB,击败了5.41% 的Python3用
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        cp = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        if not digits:
            return []
        res = [""]
        for i in digits:
            tmp = []
            for s in res:
                for j in cp[i]:
                    tmp.append(s+j)
            res = tmp
        return res

# leetcode submit region end(Prohibit modification and deletion)
