#  Beats 99.03% of users with Python3

import bisect 

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ll = nums[:1]

        for elem in nums[1:]:
            index = bisect.bisect_right(ll, elem)
            if index == 0:
                ll[0] = min(ll[0], elem)
            elif elem != ll[index - 1]:
                if index == len(ll):
                    ll.append(elem)
                else:
                    ll[index] = min(ll[index], elem)
        return len(ll)
