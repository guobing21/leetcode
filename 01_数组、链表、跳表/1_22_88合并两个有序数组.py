# 给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。
#
#
#
#  说明:
#
#
#  初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
#  你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
#
#
#
#
#  示例:
#
#  输入:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
#
# 输出: [1,2,2,3,5,6]
#  Related Topics 数组 双指针


# leetcode submit region begin(Prohibit modification and deletion)
# 1 解答成功: 执行耗时:44 ms,击败了47.02% 的Python3用户 内存消耗:13.6 MB,击败了6.90% 的Python3用户
# 时间复杂度 : O(n + m)O(n+m)
# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         nums1_copy = nums1[:m]
#         nums1[::] = []
#         p1, p2 = 0, 0
#         while p1 < m and p2 < n:
#             if nums1_copy[p1] < nums2[p2]:
#                 nums1.append(nums1_copy[p1])
#                 p1 += 1
#             else:
#                 nums1.append(nums2[p2])
#                 p2 += 1
#         if p1 < m:
#             nums1 += nums1_copy[p1:]
#         else:
#             nums1 += nums2[p2:]

# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         nums1_copy = nums1[:m]
#         nums1[::] = []
#         p1, p2 = 0, 0
#         while p1 < m and p2 < n:
#             if nums1_copy[p1] < nums2[p2]:
#                 nums1.append(nums1_copy[p1])
#                 p1 += 1
#             else:
#                 nums1.append(nums2[p2])
#                 p2 += 1
#         if p1 < m:
#             nums1[p1+p2:]= nums1_copy[p1:]
#         else:
#             nums1[p1+p2:] = nums2[p2:]
# 2 解答成功: 执行耗时:40 ms,击败了70.29% 的Python3用户 内存消耗:13.8 MB,击败了6.90% 的Python3用户
# O((n+m)log(n+m))
# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         nums1[::] = sorted(nums1[:m] + nums2)


# leetcode submit region end(Prohibit modification and deletion)
