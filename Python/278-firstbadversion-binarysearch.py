# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 0 
        right = n
        while left != right:
            midpt = left + (right - left)//2
            if isBadVersion(midpt) == True: 
                right = midpt # it's not right - 1 because first bad version might be at right index
            else: 
                left = midpt + 1 
        return right
    
        '''
        if isBadVersion(n-1) == False: 
            return n 
        else: 
            temp_num = n 
            while isBadVersion(temp_num) == True: 
                temp_num -= 1 
            return temp_num + 1 
        '''