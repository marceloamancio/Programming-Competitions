class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        copy = False
        j = 0

        for i, elem in enumerate(nums):
            if elem != val:
                nums[j] = nums[i]
                j += 1
   

        return j