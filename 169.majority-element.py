#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # My initial solution was to use a hashmap to count the number of occurrences of each number
        # Then return the key with largest value

        '''
        My initial solution was to use a hashmap to count the no. of occurrences of each number
        Then return the key with largest value
        '''

        # Using Boyer-Moore Voting Algorithm

        # Holds most common value
        candidate = nums[0]
        # Holds the number of occurrences of the current candidate
        # It counts how many more occurrences the current candidate has compared to other candidates
        count = 0

        for n in nums:
            # Increment occurrence if it matches or decrement if it's another value            
            count += 1 if candidate == n else -1
            
            # If count is negative, it means that there is a more common number
            if count == 0:
                candidate = n
                count += 1

        return candidate
        
# @lc code=end

