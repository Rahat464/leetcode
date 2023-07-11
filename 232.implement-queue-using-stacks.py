#
# @lc app=leetcode id=232 lang=python3
#
# [232] Implement Queue using Stacks
#

# @lc code=start
class MyQueue:

    def __init__(self):
        # stack1 will be used to store the list as LIFO
        # stack2 will be used as a "container" to reverse the stack and turn it into FIFO
        self.stack1 = []
        self.stack2 = []
        

    def push(self, x: int) -> None:
        # While stack1 is not empty, reverse the stack by using stack2 as a container
        while self.stack1:
            self.stack2.append(self.stack1.pop())

        # Add x to start of stack
        self.stack1.append(x)

        # Reverse stack2 into stack1 so that stack1 now has correct order
        while self.stack2:
            self.stack1.append(self.stack2.pop())


    def pop(self) -> int:
        top_element = self.stack1[-1]
        del self.stack1[-1]
        return top_element

    def peek(self) -> int:
        return self.stack1[-1]

    def empty(self) -> bool:
        return not self.stack1
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

