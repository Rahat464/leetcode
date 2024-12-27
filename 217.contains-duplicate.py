#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Solution 1: O(nlogn) time and O(1) memory
        # Sort numbers in ascending order
        nums.sort()
        for n in range(len(nums)-1):
            # Check that each number is equal to the next number
            # If equal, it means there is a duplicate
            if nums[n] == nums[n+1]: return True
        return False
    
        """
        #Solution 2: O(n) time and memory
        seen = set()
            for num in nums:
                if num in seen:
                    return True
                seen.add(num)
            return False
        """
# @lc code=end

