class Solution:
    
    def solution_99_2_1(self, board: List[List[str]], words: List[str]) -> List[str]:    
        
                     
        @functools.lru_cache(None)
        def solution_99_2_2(i, j, path):
            
            # 1) terminate
            if i not in range(0, len(board)): return
            if j not in range(0, len(board[0])): return
            if board[i][j] == "#": return
            
            # 2) success
            path += board[i][j]
            if path in self.words:
                self.result.add(path)
                
            # 3) solution_99_2_2
            c = board[i][j]
            board[i][j] = "#"
            
            for x, y in [(i+1, j), (i-1, j), (i, j-1), (i, j+1)]:
                solution_99_2_2(x, y, path)
            
            board[i][j] = c
            
    
    
        self.words = set(words)
        self.result = set()
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                solution_99_2_2(i, j, "")        
        
        return self.result