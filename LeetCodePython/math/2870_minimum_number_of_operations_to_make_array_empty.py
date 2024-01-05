from collections import Counter

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        v = Counter(nums).values()
        if 1 in v:
            return -1
        return sum([(x+2)//3 for x in v])
