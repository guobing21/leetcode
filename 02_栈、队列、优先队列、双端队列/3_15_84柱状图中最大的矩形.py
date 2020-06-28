# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
#
#  求在该柱状图中，能够勾勒出来的矩形的最大面积。
#
#
#
#
#
#  以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。
#
#
#
#
#
#  图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。
#
#
#
#  示例:
#
#  输入: [2,1,5,6,2,3]
# 输出: 10
#  Related Topics 栈 数组


# leetcode submit region begin(Prohibit modification and deletion)
# 1 解答成功: 执行耗时:76 ms,击败了41.46% 的Python3用户 内存消耗:15.8 MB,击败了11.11% 的Python3用户
# class Solution:
#     def largestRectangleArea(self, heights: List[int]) -> int:
#         max_area = 0
#         stack = []
#         heights = [0] + heights + [0]
#         for i in range(len(heights)):
#             while stack and heights[stack[-1]] > heights[i]:
#                 tmp = stack.pop()
#                 max_area = max(max_area, heights[tmp] * (i - stack[-1] - 1))
#             stack.append(i)
#         return max_area
#
# 2 解答成功: 执行耗时:80 ms,击败了31.15% 的Python3用户 内存消耗:15.3 MB,击败了11.11% 的Python3用户
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = [-1]
        for i in range(len(heights)):
            while len(stack) > 1 and heights[stack[-1]] >= heights[i]:
                tmp = stack.pop()
                max_area = max(max_area, heights[tmp] * (i - stack[-1] - 1))
            stack.append(i)
        for i in range(len(stack) - 1):
            tmp = stack.pop()
            max_area = max(max_area, heights[tmp] * (len(heights) - stack[-1] - 1))
        return max_area



# leetcode submit region end(Prohibit modification and deletion)
