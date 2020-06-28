# 给定一个二叉树，返回它的 前序 遍历。
#
#  示例:
#
#  输入: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# 输出: [1,2,3]
#
#
#  进阶: 递归算法很简单，你可以通过迭代算法完成吗？
#  Related Topics 栈 树


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 1 解答成功: 执行耗时:40 ms,击败了67.31% 的Python3用户 内存消耗:13.6 MB,击败了7.14% 的Python3用户
# class Solution:
#     def preorderTraversal(self, root: TreeNode) -> List[int]:
#         res = []
#         stack = [(False, root)]
#         while stack:
#             is_visited, node = stack.pop()
#             if node is None:
#                 continue
#             if not is_visited:
#                 stack.append((False, node.right))
#                 stack.append((False, node.left))
#                 stack.append((True, node))
#             else:
#                 res.append(node.val)
#         return res

# 2 解答成功: 执行耗时:36 ms,击败了86.32% 的Python3用户 内存消耗:13.7 MB,击败了7.14% 的Python3用户
# class Solution:
#     def preorderTraversal(self, root: TreeNode) -> List[int]:
#         if not root:
#             return []
#         return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

# 3 解答成功: 执行耗时:40 ms,击败了67.31% 的Python3用户 内存消耗:13.7 MB,击败了7.14% 的Python3用户
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def helper(node):
            if node:
                res.append(node.val)
                helper(node.left)
                helper(node.right)
        helper(root)
        return res

# class Solution:
#     def helper(self, node, res):
#         if node:
#             res.append(node.val)
#             self.helper(node.left, res)
#             self.helper(node.right, res)
#
#     def preorderTraversal(self, root: TreeNode) -> List[int]:
#         res = []
#         self.helper(root, res)
#         return res

# leetcode submit region end(Prohibit modification and deletion)
