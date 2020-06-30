# 给定一个二叉树，找出其最大深度。
#
#  二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
#
#  说明: 叶子节点是指没有子节点的节点。
#
#  示例：
# 给定二叉树 [3,9,20,null,null,15,7]，
#
#      3
#    / \
#   9  20
#     /  \
#    15   7
#
#  返回它的最大深度 3 。
#  Related Topics 树 深度优先搜索


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 1 解答成功: 执行耗时:60 ms,击败了32.01% 的Python3用户 内存消耗:15.4 MB,击败了5.55% 的Python3用户
# O(N)
# 空间复杂度最坏情况O(N)，最好情况O(logN)
# class Solution:
#     def maxDepth(self, root: TreeNode) -> int:
#         if not root:
#             return 0
#         return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

# 解答成功: 2 执行耗时:60 ms,击败了32.01% 的Python3用户 内存消耗:15 MB,击败了5.55% 的Python3用户
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [(False, 1, root)]
        depth = 0
        while stack:
            flag, this_level, node = stack.pop()
            if not node:
                continue
            if not flag:
                stack.append((True, this_level, node))
                stack.append((False, this_level+1, node.right))
                stack.append((False, this_level+1, node.left))
            else:
                depth = max(depth, this_level)
        return depth
# leetcode submit region end(Prohibit modification and deletion)
