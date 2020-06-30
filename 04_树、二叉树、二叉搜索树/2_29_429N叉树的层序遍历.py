# 给定一个 N 叉树，返回其节点值的层序遍历。 (即从左到右，逐层遍历)。
#
#  例如，给定一个 3叉树 :
#
#
#
#
#
#
#
#  返回其层序遍历:
#
#  [
#      [1],
#      [3,2,4],
#      [5,6]
# ]
#
#
#
#
#  说明:
#
#
#  树的深度不会超过 1000。
#  树的节点总数不会超过 5000。
#  Related Topics 树 广度优先搜索


# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


# 1 解答成功: 执行耗时:60 ms,击败了88.66% 的Python3用户 内存消耗:15.8 MB,击败了50.00% 的Python3用户
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        stack = [[root]]
        while stack:
            nodes = stack.pop(0)
            this_level = []
            next_level = []
            for node in nodes:
                if not node:
                    continue
                this_level += [node.val]
                next_level += node.children
            if this_level:
                res.append(this_level)
            if next_level:
                stack.append(next_level)
        return res

# leetcode submit region end(Prohibit modification and deletion)
