class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq = {} #  {letter: frequency}
        res = ""

        for char in s:
            if char in freq: freq[char] += 1
            else: freq[char] = 1
        
        for char in order:
            if char in freq:
                res += (char*freq[char])
                del freq[char]
        
        for key,value in freq.items():
            res += (key * value)

        return res