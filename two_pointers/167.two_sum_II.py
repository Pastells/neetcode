from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L, r = 0, len(numbers) - 1
        while L < r:
            s = numbers[L] + numbers[r]
            if s == target:
                return [L + 1, r + 1]
            elif s < target:
                L += 1
            else:
                r -= 1
