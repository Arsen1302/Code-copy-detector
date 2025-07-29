class Solution:
    def solution_142_1_1(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def solution_142_1_2(board, i, j):
            return (0 <= i < len(board)) and (0 <= j < len(board[0])) and board[i][j] % 10 == 1
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                for d in directions:
                    board[i][j] += 10 if solution_142_1_2(board, i + d[0], j + d[1]) else 0 # if adj cell is neighbor, add 10
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                neighbors = board[i][j] // 10 # count of neighbors
                is_live = board[i][j] % 10 == 1 # state is live or not
                if is_live: # live(1)
                    if neighbors < 2:   # Rule 1
                        board[i][j] = 0
                    elif neighbors > 3: # Rule 3
                        board[i][j] = 0
                    else:               # Rule 2
                        board[i][j] = 1
                else: # dead(0)
                    if neighbors == 3:  # Rule 4
                        board[i][j] = 1
                    else:
                        board[i][j] = 0