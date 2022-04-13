class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        new_board = [[-1 for x in range(len(board[0]))] for y in range(len(board))]
        

        
        for i in range(len(board)):
            for j in range(len(board[0])): 
                neighbor_coord = []
                results = []
                for k in [-1,0,1]:
                    for l in [-1,0,1]: 
                        if 0 <= i + k < len(board) and 0 <= j + l < len(board[0]):
                            if (i + k != i) or (j + l != j): 
                                neighbor_coord.append([i+k, j+l, board[i+k][j+l]])
                                results.append(board[i+k][j+l])
                live_neighbors = sum(results)
                if board[i][j] == 0: 
                    if live_neighbors == 3: 
                        new_board[i][j] = 1
                    else: 
                        new_board[i][j] = 0
                else: 
                    if live_neighbors < 2: 
                        new_board[i][j] = 0
                    elif 2 <= live_neighbors <= 3:
                        new_board[i][j] = 1
                    else:
                        new_board[i][j] = 0
        print(new_board)
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = new_board[i][j]