from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i, num in enumerate(nums):
            diff = target-num
            if diff in hash:
                return [i, hash[diff]]
            else:
                hash[num] = i

        return [-1, -1]
