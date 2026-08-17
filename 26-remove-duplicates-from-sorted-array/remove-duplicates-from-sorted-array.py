class Solution(object):
    def removeDuplicates(self, nums):
        n = len(nums)
        unique = 0
        for i in range(1,n):
            if nums[unique]==nums[i]:
                continue
            else:
                unique+=1
                nums[unique]=nums[i]
        return unique+1
        
        