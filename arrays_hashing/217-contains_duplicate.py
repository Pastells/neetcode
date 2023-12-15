class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        freqs = {}
        for num in nums:
            if num in freqs:
                return True
            freqs[nums] = 1

        return False
