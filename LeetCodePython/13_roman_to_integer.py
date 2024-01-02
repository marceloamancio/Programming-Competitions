simbols = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
class Solution:

    def romanToInt(self, s: str) -> int:
        n = 0

        last_v = 2000
        for ch in s:
            v = simbols[ch]

            n += v

            if v > last_v:
                n-= 2 * last_v
            

            last_v = v
        return n