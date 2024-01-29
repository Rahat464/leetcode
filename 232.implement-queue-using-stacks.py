#
# @lc app=leetcode id=232 lang=python3
#
# [232] Implement Queue using Stacks
#

# @lc code=start
class MyQueue:
    # We push to enqueue to stack1 and dequeue from stack2
    # When stack2 is empty, we reverse stack1 into stack2
    # This will lead to O(1) amortized time complexity for push and pop
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None: # aka enqueue
        self.stack1.append(x)
    
    # Helper function to reverse stack1 into stack2
    def reverse(self):
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        

    def pop(self) -> int:
        if not self.stack2: self.reverse()
        
        # Pop from stack2
        # Alternate solution would be to use built in pop() method
        tmp = self.stack2[-1]    
        del self.stack2[-1]
        return tmp

    def peek(self) -> int:
        if not self.stack2: self.reverse()

        return self.stack2[-1]

    def empty(self) -> bool:
        return True if not (self.stack1 or self.stack2) else False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

""" Old O(n) soluion
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
"""