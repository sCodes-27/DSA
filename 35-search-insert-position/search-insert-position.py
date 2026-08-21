class Solution(object):
    def searchInsert(self, nums, target):
        n = len(nums)
        st = 0
        end = n-1
        while st <= end:
            mid = st + (end-st)//2
            if nums[mid]==target:
                return mid
            elif nums[mid] <target:
                st = mid+1
            else:
                end = mid-1
        return st

        