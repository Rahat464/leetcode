#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        fast = len(numbers) - 1
        slow = 0

        while slow < fast:
            currSum = numbers[slow] + numbers[fast]
            if currSum == target:
                return [slow+1, fast+1]
            elif currSum < target: slow += 1
            else: fast -= 1
        
        return [0,0]
# @lc code=end

