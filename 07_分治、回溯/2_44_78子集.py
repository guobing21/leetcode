# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
#
#  说明：解集不能包含重复的子集。
#
#  示例:
#
#  输入: nums = [1,2,3]
# 输出:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]
#  Related Topics 位运算 数组 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
# 1.1 解答成功: 执行耗时:44 ms,击败了49.15% 的Python3用户 内存消耗:13.8 MB,击败了5.72% 的Python3用户
# 遍历
# 时间复杂度：O(N×2^N)，生成所有子集，并复制到输出结果中。
# 空间复杂度：O(N×2^N)，这是子集的数量。
# 对于给定的任意元素，它在子集中有两种情况，存在或者不存在（对应二进制中的 0 和 1）。因此，N 个数字共有 2^N个子集。
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         result = [[]]
#         for n in nums:
#             new_set = []
#             for subset in result:
#                 new_subset = subset + [n]
#                 new_set.append(new_subset)
#             result += new_set
#         return result

# 1.2
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         output = [[]]
#         for num in nums:
#             output += [curr + [num] for curr in output]
#         return output

# 2
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         def helper(level, max_level, tmp_res):
#             if level >= max_level:
#                 return
#             res.append(tmp_res)
#             new_tem_res = tmp_res + [nums[level]]
#             res.append(new_tem_res)
#             helper(level+1, max_level, new_tem_res)
#         helper(0, len(nums), [])
#         return res
#

# 2.1 解答成功: 执行耗时:40 ms,击败了73.13% 的Python3用户 内存消耗:13.9 MB,击败了5.72% 的Python3用户
# class Solution:
#     def subsets(self, nums):
#         ans = []
#         if nums == None:
#             return ans
#         self.dfs(ans, nums, [], 0)
#         return ans
#
#     def dfs(self, ans, nums, list_, index):
#         if index == len(nums):
#             ans.append(list_)
#             return
#         self.dfs(ans, nums, list_, index + 1)
#         list_.append(nums[index])
#         self.dfs(ans, nums, list_.copy(), index + 1)
#         del list_[-1]
# 2.2 解答成功: 执行耗时:44 ms,击败了49.15% 的Python3用户 内存消耗:13.6 MB,击败了5.72% 的Python3用户
# class Solution:
#     def subsets(self, nums):
#         ans = []
#         if nums == None:
#             return ans
#         self.dfs(ans, nums, [], 0)
#         return ans
#
#     def dfs(self, ans, nums, list_, index):
#         if index == len(nums):
#             ans.append(list_)
#             return
#         self.dfs(ans, nums, list_.copy(), index + 1)
#         list_.append(nums[index])
#         self.dfs(ans, nums, list_.copy(), index + 1)
#         ##del list_[-1]
# 2.3
#与2.1相同
# class Solution:
#     def subsets(self, nums):
#         ans = []
#         if nums == None:
#             return ans
#         self.dfs(ans, nums, [], 0)
#         return ans
#
#     def dfs(self, ans, nums, list_, index):
#         if index == len(nums):
#             ans.append(list_)
#             return
#         self.dfs(ans, nums, list_, index + 1)
#         self.dfs(ans, nums, list_+[nums[index]], index + 1)

# 3 解答成功: 执行耗时:44 ms,击败了49.15% 的Python3用户 内存消耗:13.8 MB,击败了5.72% 的Python3用户
# import itertools
# class Solution:
#     def subsets(self, nums):
#         res = []
#         for i in range(len(nums)+1):
#             for new_num in itertools.combinations(nums, i):
#                 res.append(list(new_num))
#         return res

# 4 解答成功: 执行耗时:40 ms,击败了73.13% 的Python3用户 内存消耗:13.6 MB,击败了5.72% 的Python3用
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def helper(i, tmp):
            res.append(tmp)
            for j in range(i, n):
                helper(j + 1, tmp + [nums[j]])

        helper(0, [])
        return res

# leetcode submit region end(Prohibit modification and deletion)
