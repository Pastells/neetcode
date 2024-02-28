class Solution1:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c for c in s.lower() if c.isalnum())
        return s == s[::-1]


class Solution2:
    def isPalindrome(self, s: str) -> bool:
        import re

        if s == "":
            return True

        s = s.lower()
        s = re.sub("[^a-z0-9]", "", s)
        return s == s[::-1]
