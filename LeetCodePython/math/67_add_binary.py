class Solution:
    def addBinary(self, a: str, b: str) -> str:
        s = ""
        i_a, i_b = len(a) - 1, len(b) - 1

        add_one = 0
        while (add_one or (i_a +1) or (i_b+1) ):
            ps = add_one
            add_one = 0
            if i_a + 1: 
                if a[i_a] == '1': 
                    ps = ps + 1
                i_a = i_a - 1
            if i_b + 1: 
                if b[i_b] == '1': 
                    ps = ps + 1
                i_b = i_b - 1

            s = str(ps%2) + s
            add_one = 1 if ps > 1 else 0

        if add_one:
            s = '1' + s

        return s
        