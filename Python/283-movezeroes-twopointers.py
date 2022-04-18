class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_nonzero_index = 0
        for i in range(len(nums)):
            if nums[i] != 0: 
                nums[last_nonzero_index], nums[i] = nums[i], nums[last_nonzero_index]
                last_nonzero_index += 1
        
        '''
        last_nonzero_index = -1  
        for i in range(len(nums)):
            if nums[i] != 0: 
                if last_nonzero_index == -1: 
                    nums[0], nums[i] = nums[i], nums[0]
                    last_nonzero_index = 0
                else: 
                    nums[last_nonzero_index + 1], nums[i] = nums[i], nums[last_nonzero_index+1]
                    last_nonzero_index += 1 
        '''
        