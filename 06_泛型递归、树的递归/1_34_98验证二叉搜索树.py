# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。
#
#  假设一个二叉搜索树具有如下特征：
#
#
#  节点的左子树只包含小于当前节点的数。
#  节点的右子树只包含大于当前节点的数。
#  所有左子树和右子树自身必须也是二叉搜索树。
#
#
#  示例 1:
#
#  输入:
#     2
#    / \
#   1   3
# 输出: true
#
#
#  示例 2:
#
#  输入:
#     5
#    / \
#   1   4
#      / \
#     3   6
# 输出: false
# 解释: 输入为: [5,1,4,null,null,3,6]。
#      根节点的值为 5 ，但是其右子节点值为 4 。
#
#  Related Topics 树 深度优先搜索


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 1 解答成功: 执行耗时:64 ms,击败了31.79% 的Python3用户 内存消耗:16.1 MB,击败了9.52% 的Python3用户
# 利用了二叉搜索树的中序遍历是递增的
# class Solution:
#     def isValidBST(self, root: TreeNode) -> bool:
#         stack = [(False, root)]
#         res = []
#         while stack:
#             flag, node = stack.pop()
#             if not node:
#                 continue
#             if not flag:
#                 stack.append((False, node.right))
#                 stack.append((True, node))
#                 stack.append((False, node.left))
#             else:
#                 res.append(node.val)
#                 if len(res) >= 2:
#                     if res[-1] <= res[-2]:
#                         return False
#         return True

# 2 解答成功: 执行耗时:60 ms,击败了53.11% 的Python3用户 内存消耗:16.7 MB,击败了9.52% 的Python3用户
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        self.pre = None
        def helper(node):
            if not node:
                return True
            if not helper(node.left):
                return False
            if self.pre and self.pre.val >= node.val:
                return False
            self.pre = node
            return helper(node.right)
        return helper(root)

# 3 解答成功: 执行耗时:60 ms,击败了53.11% 的Python3用户 内存消耗:16 MB,击败了9.52% 的Python3用户
# class Solution:
#     def isValidBST(self, root: TreeNode) -> bool:
#         def helper(node, min_val, max_val):
#             if not node:
#                 return True
#             if node.val >= max_val or node.val <= min_val:
#                 return False
#             return helper(node.left, min_val, node.val) and helper(node.right, node.val, max_val)
#         return helper(root, float("-inf"), float("inf"))
# leetcode submit region end(Prohibit modification and deletion)
