# 给定一个 N 叉树，返回其节点值的前序遍历。
#
#  例如，给定一个 3叉树 :
#
#
#
#
#
#
#
#  返回其前序遍历: [1,3,5,6,2,4]。
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

# 1 解答成功: 执行耗时:64 ms,击败了70.70% 的Python3用户 内存消耗:15.7 MB,击败了33.33% 的Python3用户
# class Solution:
#     def preorder(self, root: 'Node') -> List[int]:
#         res = []
#         stack = [(False, root)]
#         while stack:
#             is_visited, node = stack.pop()
#             if not node:
#                 continue
#             if not is_visited:
#                 for c in node.children[::-1]:
#                     stack += [(False, c)]
#                 stack += [(True, node)]
#             else:
#                 res.append(node.val)
#         return res
# 2 解答成功: 执行耗时:60 ms,击败了86.51% 的Python3用户 内存消耗:15.7 MB,击败了33.33% 的Python3用户
# class Solution:
#     def preorder(self, root: 'Node') -> List[int]:
#         if not root:
#             return []
#         res = [root.val]
#         for c in root.children:
#             res += self.preorder(c)
#         return res

# 3 解答成功: 执行耗时:64 ms,击败了70.70% 的Python3用户 内存消耗:15.7 MB,击败了33.33% 的Python3用户
# class Solution:
#     def preorder(self, root: 'Node') -> List[int]:
#         res = []
#         def helper(node):
#             if node:
#                 res.append(node.val)
#                 for c in node.children:
#                     helper(c)
#         helper(root)
#         return res
#
class Solution:
    def helper(self, node, res):
        if node:
            res.append(node.val)
            for c in node.children:
                self.helper(c, res)

    def preorder(self, root: 'Node') -> List[int]:
        res = []
        self.helper(root, res)
        return res

# leetcode submit region end(Prohibit modification and deletion)
