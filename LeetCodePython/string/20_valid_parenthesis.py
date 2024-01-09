open_chars = '([{'
close_chars = ")]}"

class Solution:
    def isValid(self, s: str) -> bool:
        q = ""

        for s_ in s:
            if s_ in open_chars:
                q += s_
            elif len(q) and close_chars[open_chars.index(q[-1])] == s_:
                q = q[:-1]
            else:
                return False

        return not len(q)
