# 反转一个单链表。
#
#  示例:
#
#  输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL
#
#  进阶:
# 你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
#  Related Topics 链表
#
#
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# 1 解答成功: 执行耗时:52 ms,击败了31.37% 的Python3用户 内存消耗:14.5 MB,击败了20.59% 的Python3用户
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         pre = None
#         while head:
#             next_node = head.next
#             head.next = pre
#             pre = head
#             head = next_node
#         return pre
#
# 2 解答成功: 执行耗时:40 ms,击败了88.21% 的Python3用户 内存消耗:14.6 MB,击败了17.65% 的Python3用户
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         pre = None
#         while head:
#             head.next, head, pre = pre, head.next, head
#         return pre
#
# 3 解答成功: 执行耗时:52 ms,击败了31.37% 的Python3用户 内存消耗:18.6 MB,击败了5.88% 的Python3用户
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         if not head or not head.next:
#             return head
#         new_head = self.reverseList(head.next)
#         head.next.next = head
#         head.next = None
#         return new_head
#
# # leetcode submit region end(Prohibit modification and deletion)
