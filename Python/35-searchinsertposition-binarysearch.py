class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums) - 1 
        
        while left < right: 
            mid = left + (right - left)//2
            if nums[mid] == target: 
                return mid 
            elif nums[mid] < target: 
                left = mid + 1 
            else: 
                right = mid - 1 
        if nums[left] < target: 
            return left + 1 # number should be next
        else: 
            return left # number should replace the current number 
        
        #return mid