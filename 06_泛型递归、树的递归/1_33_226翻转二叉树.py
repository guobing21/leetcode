# 翻转一棵二叉树。
#
#  示例：
#
#  输入：
#
#       4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
#
#  输出：
#
#       4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1
#
#  备注:
# 这个问题是受到 Max Howell 的 原问题 启发的 ：
#
#  谷歌：我们90％的工程师使用您编写的软件(Homebrew)，但是您却无法在面试时在白板上写出翻转二叉树这道题，这太糟糕了。
#  Related Topics 树


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 1 解答成功: 执行耗时:36 ms,击败了87.75% 的Python3用户 内存消耗:13.6 MB,击败了5.26% 的Python3用户
# 时间复杂度：每个元素都必须访问一次，所以是O(n)
# 空间复杂度：最坏的情况下，需要存放O(h)个函数调用(h是树的高度)，所以是O(h)
# 深度优先
# class Solution:
#     def invertTree(self, root: TreeNode) -> TreeNode:
#         if not root:
#             return
#         root.left, root.right = root.right, root.left
#         self.invertTree(root.left)
#         self.invertTree(root.right)
#         return root

# 2 解答成功: 执行耗时:40 ms,击败了71.00% 的Python3用户 内存消耗:13.8 MB,击败了5.26% 的Python3用户
# 时间复杂度：同样每个节点都需要入队列/出队列一次，所以是O(n)
# 空间复杂度：最坏的情况下会包含所有的叶子节点，完全二叉树叶子节点是n/2个，所以时间复杂度是0(n)
# 深度优先遍历的特点是一竿子插到底，不行了再退回来继续；而广度优先遍历的特点是层层扫荡。
# 广度优先
from collections import deque
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        queue = deque([root])
        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root
# leetcode submit region end(Prohibit modification and deletion)
