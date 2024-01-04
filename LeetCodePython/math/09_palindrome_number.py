class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True

        if x < 0 or (x % 10 == 0):
            return False

        m, r = 0, 0
        l = x

        while l > r:

            m = l % 10
            l = l // 10

            if l == r:
                return True

            r = (r * 10) + m

            if l == r:
                return True

        return False
