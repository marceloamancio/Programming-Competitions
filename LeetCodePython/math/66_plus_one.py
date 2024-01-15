class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        plus_one = 1
        for i in range(len(digits)):
            ir = len(digits)-i-1
            newd = digits[ir] + plus_one 
            digits[ir] = newd%10
            plus_one = 1 if newd > 9 else 0

        if plus_one:
            digits = [1] + digits

        return digits
