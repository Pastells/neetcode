from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # firts compute prefix and then postfix

        # prefix
        mult = [1]
        for n in nums[:-1]:
            mult.append(mult[-1] * n)

        # postfix
        ll = len(mult)
        k = 1
        for i, n in enumerate(nums[::-1][:-1]):
            k *= n
            mult[ll - i - 2] *= k
        return mult
