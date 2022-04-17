class Solution(object):
    def countNegatives(self, grid):
        m = len(grid) - 1  
        n = len(grid[0]) - 1 
        
        total_neg_numbers = 0 
        
        while grid[m][n] < 0 and m >= 0:
            l = 0
            r = len(grid[m])-1
            negItems = 0
            while l<=r:
                mid = l + (r-l)//2
                if grid[m][mid] < 0:
                    negItems = len(grid[m])-mid
                    r = mid-1
                elif grid[m][mid] >= 0:
                    l = mid+1
            total_neg_numbers += negItems 
            m -= 1 
        return total_neg_numbers
        
        '''
        totalNegItems = 0
        for i in grid:
            l = 0
            r = len(i)-1
            negItems = 0
            while l<=r:
                mid = l + (r-l)//2
                if i[mid] < 0:
                    negItems = len(i)-mid
                    r = mid-1
                elif i[mid] >= 0:
                    l = mid+1
            totalNegItems += negItems 
        return totalNegItems
        '''
        
        '''
        m = len(grid) - 1  
        n = len(grid[0]) - 1 
        
        total_neg_numbers = 0 
        
        while grid[m][n] < 0 and m >= 0:
            while grid[m][n] < 0 and n >= 0: 
                total_neg_numbers += 1 
                n -= 1 
            m -= 1 
            n = len(grid[0]) - 1
        return total_neg_numbers
        '''