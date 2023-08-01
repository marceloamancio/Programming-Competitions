class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        m[nums[0]] = 0

        for i in range(1,len(nums)):
            diff = target - nums[i]

            if diff in m:
                return [i, m[diff]]

            m[nums[i]] = i
