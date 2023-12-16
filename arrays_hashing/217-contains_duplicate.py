class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        freqs = {}
        for num in nums:
            if num in freqs:
                return True
            freqs[num] = 1
        
        return False
