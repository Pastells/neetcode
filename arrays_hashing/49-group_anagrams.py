from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        res = defaultdict(list)  # charCount: list of anagrams
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1  # unicode

            # count is a list (unhashable), so we use a tuple
            res[tuple(count)].append(s)

        return res.values()
