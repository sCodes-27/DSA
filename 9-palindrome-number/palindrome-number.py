class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        org= x
        rev = 0
        while(org>0):
            dig = org % 10
            org = org //10
            rev = rev*10 +dig
        if rev == x :
            return True
        else:
            return False

