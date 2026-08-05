class Solution(object):
    def maxArea(self, height):
        lp = 0
        rp = len(height)-1
        ans = 0
        while(lp<rp):
            width = rp-lp
            ht = min(height[lp],height[rp])
            area = width*ht
            ans = max(ans,area)
            if height[lp]<height[rp]:
                lp+=1
            else:
                rp-=1
        return ans