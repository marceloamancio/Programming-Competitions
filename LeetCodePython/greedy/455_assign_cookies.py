# Runtime: Beats 99.48% of users with Python3
def next_cookie(ll):
    for cookie in ll:
        yield cookie

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        counter = 0

        # Iter only once
        cookie_iterator = iter(next_cookie(sorted(s)))

        for children in sorted(g):
            for cookie in cookie_iterator:
                if cookie >= children:
                    counter += 1
                    break

        return counter