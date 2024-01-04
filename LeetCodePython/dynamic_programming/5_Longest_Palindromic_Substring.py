class Solution:
    def longestPalindrome(self, s: str) -> str:
        d = [[True for _ in range(len(s) - i + 1) ] for i in range(0,2)]

        last_has_pal = True
        for i in range(2, len(s)+1):
            ll = []
            for j in range(0, len(s) - i + 1):
                ll.append((s[j] == s[j + i - 1]) and d[i-2][j+1])

            if any(ll):
                d.append(ll)
                last_has_pal = True
            elif last_has_pal:
                d.append(ll)
                last_has_pal = False
            else:
                break

        if not last_has_pal:
            d = d[:-1]

        size = len(d) - 1
        start_pos = d[-1].index(True)
        return s[start_pos: start_pos + size]
