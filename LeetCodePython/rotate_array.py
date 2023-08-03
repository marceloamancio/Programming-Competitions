import copy 

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        k = k % len(nums)
        if k == 0:
            return 

        nums_aux = copy.copy(nums[len(nums) - k:] + nums[:len(nums) - k + 1])

        for i in range(len(nums)):
            nums[i] = nums_aux[i]
