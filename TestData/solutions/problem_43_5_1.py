class Solution:
    def solution_43_5_1(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def solution_43_5_2(r, c):
		
            q = deque([(r,c)])
            
			while q:        
                r, c = q.popleft()
                if board[r][c] == 'O':
                    board[r][c] = 'N'
                    
					for dr, dc in [[r+1,c], [r-1,c], [r,c+1], [r,c-1]]:
                        if (dr in range(len(board)) and dc in range(len(board[0])) 
							and board[dr][dc] == 'O'):
                            
							q.append((dr, dc))
        
        
        n, m = len(board), len(board[0])
        
        for i in range(m):
            if board[0][i] == 'O': solution_43_5_2(0, i)
            if board[n-1][i] == 'O': solution_43_5_2(n-1, i)
                
        for i in range(n):
            if board[i][0] == 'O': solution_43_5_2(i, 0)
            if board[i][m-1] == 'O': solution_43_5_2(i, m-1)
    
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'X': continue
                elif board[i][j] == 'N': board[i][j] = 'O' 
                else: board[i][j] = 'X'