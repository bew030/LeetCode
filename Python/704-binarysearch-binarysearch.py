class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums) -1 
        
        while left <= right: 
            pivot = left + (right-left)//2
            if nums[pivot] == target:
                return pivot 
            elif target < nums[pivot]:
                right = pivot-1
            else: 
                left = pivot + 1 
        return -1 
        
        '''
        middle_num = len(nums)//2
        increase = False 
        decrease = False
        
        while -1 < middle_num < len(nums):
            if nums[middle_num] == target:
                return middle_num
            elif nums[middle_num] > target:
                if increase == True: 
                    return -1 
                decrease = True 
                middle_num -= 1 
            elif nums[middle_num] < target: 
                if decrease == True:
                    return -1 
                increase = True 
                middle_num += 1 
        return -1 
        '''
        
        '''
        # n run time 
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1
        '''