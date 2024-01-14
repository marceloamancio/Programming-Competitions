class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        i = s.rfind(' ')
        return len(s) - i - 1
        