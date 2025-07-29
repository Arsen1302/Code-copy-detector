class Solution:
    def solution_765_2(self, target: str) -> str:
        
        # Map row and column for all characters
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]       
        map_row = {char: r for r, characters in enumerate(board) for c, char in enumerate(characters)}
        map_col = {char: c for r, characters in enumerate(board) for c, char in enumerate(characters)}
                
        res = []
        r = c = 0
        for char in target:
            target_r, target_c = map_row[char], map_col[char]

            if r != target_r or c != target_c:
                if r == 5 and c == 0: # special case: if at 'z', can only move up
                    res.append('U')
                    r -= 1
                    
				# Go to target column
                hori_move = abs(target_c - c)
                res.append('R' * hori_move if c < target_c else 'L' * hori_move)
                if c > target_c: 
                    hori_move *= -1
                c += hori_move
                          
				# Go to target row
                verti_move = abs(target_r - r)
                res.append('D' * verti_move if r < target_r else 'U' * verti_move)
                if r > target_r:  verti_move *= -1   
                r += verti_move
                    
            res.append('!')
        
        return ''.join(res)