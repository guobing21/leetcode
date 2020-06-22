# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
#
#
#
#  示例：
#
#  输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
#
#  Related Topics 链表


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 1 解答成功: 执行耗时:48 ms,击败了55.32% 的Python3用户 内存消耗:13.7 MB,击败了7.14% 的Python3用户
# O(n+m), O(1)
# class Solution:
#     def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
#         hair = ListNode(-1)
#         pre = hair
#         while l1 and l2:
#             if l1.val < l2.val:
#                 pre.next = l1
#                 l1 = l1.next
#             else:
#                 pre.next = l2
#                 l2 = l2.next
#             pre = pre.next
#         pre.next = l1 if l1 else l2
#         return hair.next

# 2 解答成功: 执行耗时:52 ms,击败了31.38% 的Python3用户 内存消耗:13.5 MB,击败了7.14% 的Python3用
# O(n+m), O(n+m)
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        elif not l2:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

# leetcode submit region end(Prohibit modification and deletion)
