class Solution:
    def solution_1379_4_1(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        
        def solution_1379_4_2(seq, word):
            if len(seq) != len(word):
                return False
            forward, reverse = True, True
            for i in range(len(seq)):
                if seq[i] != ' ' and seq[i] != word[i]:
                    forward = False
                if seq[-1-i] != ' ' and seq[-1-i] != word[i]:
                    reverse = False
            return forward or reverse
        
        vertical = set()
        horizontal = set()
        for r in range(m):
            for c in range(n):
                if board[r][c] == '#':
                    continue
                
                if (r, c) not in vertical:
                    seq, i = '', 0
                    while r + i < m and board[r+i][c] != '#':
                        vertical.add((r+i, c))
                        seq += board[r+i][c]
                        i += 1
                    
                    if solution_1379_4_2(seq, word):
                        return True
                
                if (r, c) not in horizontal:
                    seq, i = '', 0
                    while c + i < n and board[r][c+i] != '#':
                        horizontal.add((r, c+i))
                        seq += board[r][c+i]
                        i += 1
                    
                    if solution_1379_4_2(seq, word):
                        return True
        
        return False