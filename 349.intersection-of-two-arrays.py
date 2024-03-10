class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = set(nums2)
        res = []
        
        for n in nums1:
            if n in seen:
                res.append(n)
                seen.remove(n)
        
        return res