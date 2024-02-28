"""
# this would be a valid solution
from collections import Counter
return Counter(s) == Counter(t)
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def count(word: str) -> dict:
            hash = {}
            for c in word:
                hash[c] = hash.get(c, 0) + 1
            return hash

        if len(s) != len(t):
            return False

        return count(s) == count(t)
