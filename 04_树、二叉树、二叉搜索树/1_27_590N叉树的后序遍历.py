# 给定一个 N 叉树，返回其节点值的后序遍历。
#
#  例如，给定一个 3叉树 :
#
#
#
#
#
#
#
#  返回其后序遍历: [5,6,3,2,4,1].
#
#
#
#  说明: 递归法很简单，你可以使用迭代法完成此题吗? Related Topics 树


# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


# 1 解答成功: 执行耗时:68 ms,击败了48.35% 的Python3用户 内存消耗:15.8 MB,击败了33.33% 的Python3用户
# class Solution:
#     def postorder(self, root: 'Node') -> List[int]:
#         res = []
#         stack = [(False, root)]
#         while stack:
#             is_visited, node = stack.pop()
#             if not node:
#                 continue
#             if not is_visited:
#                 stack += [(True, node)]
#                 for c in node.children[::-1]:
#                     stack += [(False, c)]
#             else:
#                 res.append(node.val)
#         return res

# 2 解答成功: 执行耗时:72 ms,击败了30.74% 的Python3用户 内存消耗:15.5 MB,击败了33.33% 的Python3用户
# class Solution:
#     def postorder(self, root: 'Node') -> List[int]:
#         if not root:
#             return []
#         res = []
#         for c in root.children:
#             res += self.postorder(c)
#         return res + [root.val]

# 3 解答成功: 执行耗时:60 ms,击败了84.70% 的Python3用户 内存消耗:15.6 MB,击败了33.33% 的Python3用户
# class Solution:
#     def postorder(self, root: 'Node') -> List[int]:
#         res = []
#         def helper(node):
#             if node:
#                 for c in node.children:
#                     helper(c)
#                 res.append(node.val)
#         helper(root)
#         return res

# 4 解答成功: 执行耗时:60 ms,击败了84.70% 的Python3用户 内存消耗:15.7 MB,击败了33.33% 的Python3用户
class Solution:
    def helper(self, node, res):
        if node:
            for c in node.children:
                self.helper(c, res)
            res += [node.val]

    def postorder(self, root: 'Node') -> List[int]:
        res = []
        self.helper(root, res)
        return res

# leetcode submit region end(Prohibit modification and deletion)
