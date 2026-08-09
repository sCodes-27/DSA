class Solution(object):
    def search(self, nums, target):
        st = 0
        end = len(nums)-1
        while(st<=end):
            mid = st + (end-st)//2
            if nums[mid] == target:
                return mid
            if nums[mid]>=nums[st]:
                if target >=nums[st] and target <= nums[mid]:
                    end = mid-1
                else:
                    st = mid +1
            else:
                if target >= nums[mid] and target <= nums[end]:
                    st = mid+1
                else:
                    end = mid -1
        return -1

        