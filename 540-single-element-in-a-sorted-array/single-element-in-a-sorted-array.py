class Solution(object):
    def singleNonDuplicate(self, nums):
        n = len(nums)
        st = 0 
        end =n-1
        if n==1:
            return nums[0]
        while(st<=end):
            mid = st + (end-st)//2
            if mid == 0 and nums[0]!=nums[1]:
                return nums[mid]
            elif mid == n-1 and nums[n-1]!=nums[n-2]:
                return nums[mid]
            if nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]:
                return nums[mid]
            elif mid %2==0:
                if nums[mid]==nums[mid-1]:
                    end = mid-1
                else:
                    st = mid+1
            else:
                if nums[mid]==nums[mid-1]:
                    st = mid+1
                else:
                    end = mid-1
