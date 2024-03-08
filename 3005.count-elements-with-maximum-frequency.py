class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        bucket = [0] * 101
        curr_max = n = 0
        
        for num in nums:
            bucket[num] += 1
            
            if curr_max == bucket[num]: n += 1
            elif curr_max < bucket[num]:
                n = 1
                curr_max  = bucket[num]
        
        return n * curr_max