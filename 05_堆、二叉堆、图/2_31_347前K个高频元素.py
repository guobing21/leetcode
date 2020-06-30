# 给定一个非空的整数数组，返回其中出现频率前 k 高的元素。
#
#
#
#  示例 1:
#
#  输入: nums = [1,1,1,2,2,3], k = 2
# 输出: [1,2]
#
#
#  示例 2:
#
#  输入: nums = [1], k = 1
# 输出: [1]
#
#
#
#  提示：
#
#
#  你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
#  你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。
#  题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的。
#  你可以按任意顺序返回答案。
#
#  Related Topics 堆 哈希表


# leetcode submit region begin(Prohibit modification and deletion)
# 1 解答成功: 执行耗时:56 ms,击败了72.54% 的Python3用户 内存消耗:16.7 MB,击败了100.00% 的Python3用户
# from collections import defaultdict
#
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         num2count = defaultdict(int)
#         for n in nums:
#             num2count[n] += 1
#         ans = sorted(num2count.items(), key=lambda x:x[1], reverse=True)[:k]
#         return [a[0] for a in ans]

# 2 解答成功: 执行耗时:52 ms,击败了83.06% 的Python3用户 内存消耗:16.6 MB,击败了100.00% 的Python3用户
# import collections
# import heapq
#
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         counter = collections.Counter(nums)
#         return heapq.nlargest(k, counter.keys(), key=counter.get)

# 3 解答成功: 执行耗时:60 ms,击败了63.85% 的Python3用户 内存消耗:16.6 MB,击败了100.00% 的Python3用户
import collections
import heapq

class Solution:
    def topKFrequent(self, nums, k) :
        counter = collections.Counter(nums)
        c_n = [(c, n) for c, n in zip(counter.values(), counter.keys())]
        hp = c_n[:k]
        heapq.heapify(hp)
        for i in range(k, len(c_n)):
            if hp[0] < c_n[i]:
                heapq.heappop(hp)
                heapq.heappush(hp, c_n[i])
        return [n for c,n in hp]

# leetcode submit region end(Prohibit modification and deletion)
