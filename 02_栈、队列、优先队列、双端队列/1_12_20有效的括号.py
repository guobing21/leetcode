# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
#
#  有效字符串需满足：
#
#
#  左括号必须用相同类型的右括号闭合。
#  左括号必须以正确的顺序闭合。
#
#
#  注意空字符串可被认为是有效字符串。
#
#  示例 1:
#
#  输入: "()"
# 输出: true
#
#
#  示例 2:
#
#  输入: "()[]{}"
# 输出: true
#
#
#  示例 3:
#
#  输入: "(]"
# 输出: false
#
#
#  示例 4:
#
#  输入: "([)]"
# 输出: false
#
#
#  示例 5:
#
#  输入: "{[]}"
# 输出: true
#  Related Topics 栈 字符串
#
#
# leetcode submit region begin(Prohibit modification and deletion)
# 1 解答成功: 执行耗时:44 ms,击败了55.06% 的Python3用户 内存消耗:13.7 MB,击败了5.22% 的Python3用户
class Solution:
    def isValid(self, s: str) -> bool:
        stack = ["?"]
        pun_cp = {"(" : ")", "[" : "]", "{" : "}", "?" : "?"}
        for i in s:
            if i in pun_cp:
                stack.append(i)
            elif i != " ":
                if pun_cp[stack.pop()] != i:
                    return False
        return len(stack) == 1
# 2 解答成功: 执行耗时:44 ms,击败了55.06% 的Python3用户 内存消耗:13.7 MB,击败了5.22% 的Python3用户
# class Solution:
#     def isValid(self, s: str) -> bool:
#         while "()" in s or "[]" in s or "{}" in s:
#             s = s.replace("()", "")
#             s = s.replace("[]", "")
#             s = s.replace("{}", "")
#         return not s
#
# leetcode submit region end(Prohibit modification and deletion)
