# # 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复
# # 的三元组。
# #
# #  注意：答案中不可以包含重复的三元组。
# #
# #
# #
# #  示例：
# #
# #  给定数组 nums = [-1, 0, 1, 2, -1, -4]，
# #
# # 满足要求的三元组集合为：
# # [
# #   [-1, 0, 1],
# #   [-1, -1, 2]
# # ]
# #
# #  Related Topics 数组 双指针
#
#
# # leetcode submit region begin(Prohibit modification and deletion)
# 1.1 解答成功: 执行耗时:796 ms,击败了84.01% 的Python3用户 内存消耗:16.3 MB,击败了10.84% 的Python3用户
# O(n^2)
# 排序的目的是为了避免有重复结果，如果用set存储答案不排序也行。
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         res_nums = []
#         nums.sort()
#         for i in range(len(nums)-2):
#             if nums[i] > 0:
#                 return res_nums
#             if i > 0 and nums[i] == nums[i-1]:
#                 continue
#             left, right = i+1, len(nums)-1
#             while left < right:
#                 if nums[i] + nums[left] + nums[right] < 0:
#                     left += 1
#                 elif nums[i] + nums[left] + nums[right] > 0:
#                     right -= 1
#                 else:
#                     res_nums.append([nums[i], nums[left], nums[right]])
#                     while True:
#                         left += 1
#                         if left >= right or nums[left] > nums[left-1]:
#                             break
#                     while True:
#                         right -= 1
#                         if right <= left or nums[right] < nums[right+1]:
#                             break
#         return res_nums

# 1.2 解答成功: 执行耗时:932 ms,击败了73.25% 的Python3用户 内存消耗:16.4 MB,击败了28.22% 的Python3用户
# class Solution:
#     def threeSum(self, nums: [int]) -> [[int]]:
#         nums.sort()
#         res, k = [], 0
#         for k in range(len(nums) - 2):
#             if nums[k] > 0: break # 1. because of j > i > k.
#             if k > 0 and nums[k] == nums[k - 1]: continue # 2. skip the same `nums[k]`.
#             i, j = k + 1, len(nums) - 1
#             while i < j: # 3. double pointer
#                 s = nums[k] + nums[i] + nums[j]
#                 if s < 0:
#                     i += 1
#                     while i < j and nums[i] == nums[i - 1]: i += 1
#                 elif s > 0:
#                     j -= 1
#                     while i < j and nums[j] == nums[j + 1]: j -= 1
#                 else:
#                     res.append([nums[k], nums[i], nums[j]])
#                     i += 1
#                     j -= 1
#                     while i < j and nums[i] == nums[i - 1]: i += 1
#                     while i < j and nums[j] == nums[j + 1]: j -= 1
#         return res

# 1.3 解答成功: 执行耗时:972 ms,击败了62.16% 的Python3用户 内存消耗:15.8 MB,击败了98.03% 的Python3用户
class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l +=1
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1; r -= 1
        return res

# 2 解答成功: 执行耗时:1036 ms,击败了49.20% 的Python3用户 内存消耗:16.8 MB,击败了6.02% 的Python3用户
# O(n^2)
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         res_nums = []
#         nums.sort()
#         num2id = {n:i for i,n in enumerate(nums)}
#         for i in range(len(nums)-2):
#             if nums[i] > 0:
#                 return res_nums
#             if i > 0 and nums[i] == nums[i-1]:
#                 continue
#             for j in range(i+1, len(nums)-1):
#                 if j > i + 1 and nums[j] == nums[j-1]:
#                     continue
#                 add2 = nums[i] + nums[j]
#                 k = num2id.get(-add2)
#                 if k and k > j:
#                     res_nums.append([nums[i], nums[j], nums[k]])
#         return res_nums

# 3
# 3.1 超出时间限制
# O(n^3)
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         res_nums = []
#         nums.sort()
#         for i in range(len(nums)-2):
#             if nums[i] > 0:
#                 return res_nums
#             if i > 0 and nums[i] == nums[i-1]:
#                 continue
#             for j in range(i+1, len(nums)-1):
#                 if j > i + 1 and nums[j] == nums[j-1]:
#                     continue
#                 for k in range(j+1, len(nums)):
#                     if k > j+1 and nums[k] == nums[k-1]:
#                         continue
#                     if nums[i] + nums[j] + nums[k] == 0:
#                         res_nums.append([nums[i], nums[j], nums[k]])
#         return res_nums

# 3.2 超出时间限制
# O(n^3)
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         if not nums or len(nums) <= 2:
#             return []
#         res_nums = set()
#         nums.sort()
#         for i in range(len(nums)-2):
#             for j in range(i+1, len(nums)-1):
#                 for k in range(j+1, len(nums)):
#                     if nums[i] + nums[j] + nums[k] == 0:
#                         res_nums.add((nums[i], nums[j], nums[k]))
#         return [list(r) for r in res_nums]

# # leetcode submit region end(Prohibit modification and deletion)
