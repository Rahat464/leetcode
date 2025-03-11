#
# @lc app=leetcode id=2523 lang=python3
#
# [2523] Closest Prime Numbers in Range
#

# @lc code=start
class Solution:
    def findAllPrimes(self, left, right) -> List[int]:
        isPrime: list[int] = [True for _ in range(right+1)]
        # Edge cases
        isPrime[0] = isPrime[1] = False

        # Set all non primes to false
        for n in range(4, right+1, 2):
            isPrime[n] = False

        # Same step, but skipping all even numbers
        for n in range(3, right+1, 2):
            for m in range(n*n, right+1, n):
                isPrime[m] = False

        primes: List[int] = []
        # Set left to odd so we skip all even numbers
        if left <= 2: primes.append(2)
        left += 1 if (left % 2 == 0) else 0
    
        for i in range(left, right+1, 2):
            if isPrime[i]: primes.append(i)

        return primes

    def closestPrimes(self, left: int, right: int) -> List[int]:
        primes: List[int] = self.findAllPrimes(left, right)

        if len(primes) < 2: return [-1, -1]
        result: List[int] = [primes[0], primes[1]]

        for i in range(1, len(primes) - 1):
            num1: int = primes[i]
            num2: int = primes[i + 1]

            if (num2 - num1) < (result[1] - result[0]):
                result = [num1, num2]

        return result
        
# @lc code=end

