class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        ls:list
        ls = sorted(nums1 + nums2)
        print(ls)
        len_ls = m+n
        middle = int(len_ls / 2)
        if len_ls % 2 == 0:
            result = (ls[middle] + ls[middle-1]) / 2
            return result
        elif len_ls % 2 != 0:
            result = ls[middle]
            return result
        else:
            return ls
        