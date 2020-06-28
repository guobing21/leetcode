# 使用栈实现队列的下列操作：
#
#
#  push(x) -- 将一个元素放入队列的尾部。
#  pop() -- 从队列首部移除元素。
#  peek() -- 返回队列首部的元素。
#  empty() -- 返回队列是否为空。
#
#
#
#
#  示例:
#
#  MyQueue queue = new MyQueue();
#
# queue.push(1);
# queue.push(2);
# queue.peek();  // 返回 1
# queue.pop();   // 返回 1
# queue.empty(); // 返回 false
#
#
#
#  说明:
#
#
#  你只能使用标准的栈操作 -- 也就是只有 push to top, peek/pop from top, size, 和 is empty 操作是合法的。
#
#  你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
#  假设所有操作都是有效的 （例如，一个空的队列不会调用 pop 或者 peek 操作）。
#
#  Related Topics 栈 设计
#
#
# leetcode submit region begin(Prohibit modification and deletion)
# 解答成功: 执行耗时:44 ms,击败了38.44% 的Python3用户 内存消耗:13.8 MB,击败了11.11% 的Python3用户
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack_left = []
        self.stack_right = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        while self.stack_left:
            self.stack_right.append(self.stack_left.pop())
        self.stack_right.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        while self.stack_right:
            self.stack_left.append(self.stack_right.pop())
        return self.stack_left.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        while self.stack_right:
            self.stack_left.append(self.stack_right.pop())
        return self.stack_left[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.stack_left and not self.stack_right


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# leetcode submit region end(Prohibit modification and deletion)
