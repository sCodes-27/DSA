class Solution(object):
    def peakIndexInMountainArray(self, arr):
        st = 1
        end = len(arr)-2
        while(st <= end):
            mid = st + (end-st)//2
            if arr[mid-1]<arr[mid] and arr[mid]>arr[mid+1]:
                return mid
            elif arr[mid]>arr[mid-1]:
                st = mid+1
            else:
                end = mid-1
                    
        