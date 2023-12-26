from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for n in nums:
            counter[n] = 1 + counter.get(n, 0)

        # create a frequency bucket with the elements that appear n times
        # at most we'll have the same element len(nums) times
        freq = [[] for _ in range(len(nums) + 1)]
        for n, c in counter.items():
            freq[c].append(n)

        out = []
        i = len(nums)
        while len(out) < k:
            out.extend(freq[i])
            i -= 1

        return out
