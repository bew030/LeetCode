class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        return_matrix = [[0 for i in range(n)] for j in range(n)]
        # 0 = right, 1 = down, 2 = left, 3 = up 
        start_coord = [0,0]
        #print(start_coord)
        iterator = 1 
        return_matrix[start_coord[0]][start_coord[1]] = iterator
        iterator += 1 
        mini_loop = n
        direction = ['right','down','left','up']
        current_direction = 'right'
        first_round = True 
        while mini_loop > 0: 
            if current_direction == 'right':
                #print('right')
                for i in range(1,mini_loop):
                    start_coord[1] += 1
                    return_matrix[start_coord[0]][start_coord[1]] = iterator
                    iterator += 1 
                    #print(start_coord)
                current_direction = 'down'
                if first_round != True: 
                    mini_loop -= 1 
            elif current_direction == 'down':
                #print('down')
                for i in range(1,mini_loop):
                    start_coord[0] += 1
                    return_matrix[start_coord[0]][start_coord[1]] = iterator
                    iterator += 1
                    #print(start_coord)
                current_direction = 'left'
            elif current_direction == 'left':
                #print('left')
                for i in range(1,mini_loop):
                    start_coord[1] -= 1
                    return_matrix[start_coord[0]][start_coord[1]] = iterator
                    iterator += 1
                    #print(start_coord)
                current_direction = 'up'
                mini_loop -= 1
            else:
                #print('up')
                for i in range(1,mini_loop):
                    start_coord[0] -= 1
                    return_matrix[start_coord[0]][start_coord[1]] = iterator
                    iterator += 1
                    #print(start_coord)
                current_direction = 'right'
                first_round = False 
        return return_matrix
                
            