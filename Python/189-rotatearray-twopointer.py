class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        beginning = nums[-k%len(nums):]
        end = nums[:-k%len(nums)]
        print(beginning, end)
        result = beginning + end 
        for i in range(len(nums)):
            nums[i] = result[i]
        '''
        
        return_list = nums.copy()
        
        for i in range(len(nums)):
            index = (i+k)%len(nums)
            nums[index] = return_list[i]
