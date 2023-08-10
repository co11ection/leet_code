# Given a 0-indexed integer array nums, return true if it can be made strictly increasing after removing exactly one element, or false otherwise. If the array is already strictly increasing, return true.

# The array nums is strictly increasing if nums[i - 1] < nums[i] for each index (1 <= i < nums.length).
###########################################################################
# Учитывая 0-индексированный целочисленный массив nums, вернуть true, если его можно сделать строго возрастающим после удаления ровно одного элемента, или false в противном случае. Если массив уже строго увеличивается, вернуть true.

# Массив nums строго увеличивается, если nums[i - 1] < nums[i] для каждого индекса (1 <= i < nums.length).
############################################################################



class Solution(object):
    def canBeIncreasing(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        removed = False
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                if removed:
                    return False
                if i - 2 >= 0 and nums[i] <= nums[i - 2]:
                    if i + 1 < len(nums) and nums[i + 1] <= nums[i - 1]:
                        return False
                removed = True
        return True