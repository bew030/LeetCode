class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0 
        right = len(nums) - 1 
        
        n = len(nums)
        results = [0] * n
        # it's ideal to make the list from largest to smallest, since you know nums[0] or nums[-1] will be the largest value
        for i in range(n-1, -1, -1):
            if abs(nums[left]) < abs(nums[right]): 
                square = nums[right]
                right -= 1 
            else: 
                square = nums[left]
                left += 1 
            results[i] = square * square 
        return results
    
        '''
        nums = [x**2 for x in nums]
        nums.sort()
        
        return nums
        '''