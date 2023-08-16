class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        index = 0
        if target > nums[-1]:
            index = len(nums)
            return index
        for ind, num in enumerate(nums):
            if num == target:
                index = ind
                return index
            elif num < target:
                index = ind
                continue
            elif num > target:
                index = ind
                return index