# 给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
#
#  你可以假设数组是非空的，并且给定的数组总是存在多数元素。
#
#
#
#  示例 1:
#
#  输入: [3,2,3]
# 输出: 3
#
#  示例 2:
#
#  输入: [2,2,1,1,1,2,2]
# 输出: 2
#
#  Related Topics 位运算 数组 分治算法


# leetcode submit region begin(Prohibit modification and deletion)
# 1 哈希表
# O(n)O(n)
# 1.1 解答成功: 执行耗时:44 ms,击败了92.26% 的Python3用户 内存消耗:15.3 MB,击败了6.90% 的Python3用户
# from collections import defaultdict
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         count_dict = defaultdict(int)
#         for n in nums:
#             count_dict[n] += 1
#         res = nums[0]
#         for n in count_dict.keys():
#             if count_dict[n] > count_dict[res]:
#                 res = n
#         return res

# 1.2 解答成功: 执行耗时:44 ms,击败了92.26% 的Python3用户 内存消耗:15.2 MB,击败了6.90% 的Python3用户
# from collections import Counter
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         counter = Counter(nums)
#         return max(counter.keys(), key=counter.get)

# 2 解答成功: 执行耗时:40 ms,击败了96.99% 的Python3用户 内存消耗:15.2 MB,击败了6.90% 的Python3用户
# O(nlogn)
# O(logn):如果使用语言自带的排序算法，需要使用O(logn) 的栈空间
# 排序
# 如果将数组 nums 中的所有元素按照单调递增或单调递减的顺序排序，那么下标为n//2 的元素（下标从 0 开始）一定是众数。
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         nums.sort()
#         return nums[len(nums)//2]

# 3 解答成功: 执行耗时:180 ms,击败了5.07% 的Python3用户 内存消耗:15.8 MB,击败了6.90% 的Python3用户
# O(nlogn), O(nlogn)
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         def helper(low, high):
#             if low == high:
#                 return nums[low]
#             mid = low + (high-low)//2
#             left = helper(low, mid)
#             right = helper(mid+1, high)
#             if left == right:
#                 return left
#             left_count = sum(1 for i in range(low, high+1) if nums[i] == left)
#             right_count = sum(1 for i in range(low, high+1) if nums[i] == right)
#             return left if left_count > right_count else right
#         return helper(0, len(nums)-1)


# leetcode submit region end(Prohibit modification and deletion)
