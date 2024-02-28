from collections import defaultdict
from typing import List

import numpy as np


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)  # charCount: list of anagrams
        for s in strs:
            count = np.zeros(26)
            for c in s:
                count[ord(c) - ord("a")] += 1  # unicode

            # count is a list (unhashable), so we use a tuple
            res[tuple(count)].append(s)

        return res.values()
