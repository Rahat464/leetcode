#
# @lc app=leetcode id=1656 lang=python3
#
# [1656] Design an Ordered Stream
#

# @lc code=start
class OrderedStream:

    def __init__(self, n: int):
        self.array = [None] * (n+1)
        self.ptr = 0
        

    def insert(self, idKey: int, value: str) -> List[str]:
        self.array[idKey-1] = value

        res = []
        while self.ptr < len(self.array) and self.array[self.ptr]:
            res.append(self.array[self.ptr])
            self.ptr += 1
        
        return res

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
# @lc code=end

