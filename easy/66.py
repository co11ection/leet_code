class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        nums = ''
        for i in digits:
            nums += str(i)
        nums = int(nums) + 1
        nums = str(nums)
        result = [int(n) for n in nums]
        return result