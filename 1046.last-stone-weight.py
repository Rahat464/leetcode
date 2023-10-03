#
# @lc app=leetcode id=1046 lang=python3
#
# [1046] Last Stone Weight
#

# @lc code=start
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        # Python does not have max heaps, so invert all numbers and use min heap instead
        stones = [-s for s in stones]

        heapq.heapify(stones)

        while len(stones) > 1:
            l = heapq.heappop(stones)
            s = heapq.heappop(stones)

            heapq.heappush(stones, l - s)

        return abs(stones[0])
        
# @lc code=end

