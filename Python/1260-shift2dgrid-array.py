class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        total_shifts = k % (len(grid) * len(grid[0]))
        num_w_index = []
        index = 0 
        for i in range(len(grid)): 
            for j in range(len(grid[0])):
                potential_index = index + total_shifts
                if potential_index < (len(grid) * len(grid[0])):
                    num_w_index.append([potential_index, grid[i][j]])
                else: 
                    num_w_index.append([potential_index - (len(grid) * len(grid[0])), grid[i][j]])
                index += 1 
        num_w_index.sort(key = lambda x: x[0])
        
        return_matrix = []
        iterator = 0
        for i in range(len(grid)):
            new_row = []
            for j in range(len(grid[0])):
                new_row.append(num_w_index[iterator][1])
                iterator += 1 
            return_matrix.append(new_row)
        return return_matrix