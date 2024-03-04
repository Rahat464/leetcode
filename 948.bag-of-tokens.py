#
# @lc app=leetcode id=948 lang=python3
#
# [948] Bag of Tokens
#

# @lc code=start
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        # Neetcode 2 pointer greedy solution
        tokens.sort()
        left, right = 0, len(tokens) - 1
        score = max_score = 0

        while left <= right:
            if tokens[left] <= power:
                power -= tokens[left]
                left += 1
                score += 1
                max_score = max(max_score, score)
            
            elif score > 0:
                power += tokens[right]
                right -= 1
                score -= 1
            
            # We do not have enough score or power to play
            else: break

        return max_score
        
# @lc code=end

