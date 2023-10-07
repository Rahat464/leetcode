#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:


    def __init__(self):
        self.s = []
        self.s1 = []


    def push(self, val: int) -> None:
        if not self.s:
            self.s.append(val)
            self.s1.append(val)
        else:
            self.s.append(val)
            if self.s1[-1] < val: self.s1.append( self.s1[-1])
            else:  self.s1.append(val)


    def pop(self) -> None:
        del self.s1[-1]
        temp = self.s[-1]
        del self.s[-1]
        return temp
        

    def top(self) -> int:
        return self.s[-1]
        

    def getMin(self) -> int:
        return self.s1[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

