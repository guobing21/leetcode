# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
#
#  示例 1:
#
#  输入: [1,2,3,4,5,6,7] 和 k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右旋转 1 步: [7,1,2,3,4,5,6]
# 向右旋转 2 步: [6,7,1,2,3,4,5]
# 向右旋转 3 步: [5,6,7,1,2,3,4]
#
#
#  示例 2:
#
#  输入: [-1,-100,3,99] 和 k = 2
# 输出: [3,99,-1,-100]
# 解释:
# 向右旋转 1 步: [99,-1,-100,3]
# 向右旋转 2 步: [3,99,-1,-100]
#
#  说明:
#
#
#  尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
#  要求使用空间复杂度为 O(1) 的 原地 算法。
#
#  Related Topics 数组


# leetcode submit region begin(Prohibit modification and deletion)
# 1 运行失败: Time Limit Exceeded stdout: null
# O(kn),O(1)
# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         n = len(nums)
#         k = k % n
#         for j in range(k):
#             tmp = nums[-1]
#             for i in range(n):
#                 nums[i], tmp = tmp, nums[i]


#2 解答成功: 执行耗时:24 ms,击败了99.92% 的Python3用户 内存消耗:14 MB,击败了86.49% 的Python3用户
# 但是O(1), O(n), 不符合题意
# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         n = len(nums)
#         nums[::] = nums[n-k:] + nums[:n-k]

# 3 解答成功: 执行耗时:32 ms,击败了98.11% 的Python3用户 内存消耗:13.8 MB,击败了97.30% 的Python3用户
# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         n = len(nums)
#         k = k % n
#         left, right = 0, n - 1
#         while left < right:
#             nums[left], nums[right] = nums[right], nums[left]
#             left += 1
#             right -= 1
#         left1, right1 = 0, k - 1
#         while left1 < right1:
#             nums[left1], nums[right1] = nums[right1], nums[left1]
#             left1 += 1
#             right1 -= 1
#         left2, right2 = k, n - 1
#         while left2 < right2:
#             nums[left2], nums[right2] = nums[right2], nums[left2]
#             left2 += 1
#             right2 -= 1

# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         nums.reverse()
#         n = len(nums)
#         k = k % n
#         left1, right1 = 0, k - 1
#         while left1 < right1:
#             nums[left1], nums[right1] = nums[right1], nums[left1]
#             left1 += 1
#             right1 -= 1
#         left2, right2 = k, n - 1
#         while left2 < right2:
#             nums[left2], nums[right2] = nums[right2], nums[left2]
#             left2 += 1
#             right2 -= 1

# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         n=len(nums)
#         k=k%n
#         def swap(l,r):
#             while(l<r):
#                 nums[l],nums[r]=nums[r],nums[l]
#                 l=l+1
#                 r=r-1
#         swap(0,n-k-1)
#         swap(n-k,n-1)
#         swap(0,n-1)

# class Solution:
#     def reverse(self, nums, l, r):
#         while l < r:
#             nums[l], nums[r] = nums[r], nums[l]
#             l += 1
#             r -= 1
#
#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         n = len(nums)
#         k = k % n
#         self.reverse(nums, 0, n-1)
#         self.reverse(nums, 0, k-1)
#         self.reverse(nums, k, n-1)


# 3 解答成功: 执行耗时:152 ms,击败了6.50% 的Python3用户 内存消耗:13.9 MB,击败了89.19% 的Python3用户
# O(kn), O(1)
# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         n = len(nums)
#         k = k % n
#         for i in range(k):
#             nums.insert(0, nums.pop())

# 4 解答成功: 执行耗时:44 ms,击败了65.04% 的Python3用户 内存消耗:13.7 MB,击败了100.00% 的Python3用户
# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         n = len(nums)
#         k %= n
#         nums[:] = nums[::-1]
#         nums[:k] = nums[:k][::-1]
#         nums[k:] = nums[k:][::-1]

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        nums.reverse()
        nums[:k] = list(reversed(nums[:k]))
        nums[k:] = list(reversed(nums[k:]))

# leetcode submit region end(Prohibit modification and deletion)
