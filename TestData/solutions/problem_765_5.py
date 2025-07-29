class Solution:
    def solution_765_5(self, target: str) -> str:
        # find mapping from letter to index
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        letter2idx = {}
        for i in range(len(board)):
            for j in range(len(board[i])):
                letter2idx[board[i][j]] = (i, j)
        
        cur_i = cur_j = 0
        ret = []
        for letter in target:
            d_i = letter2idx[letter][0]-cur_i 
            d_j = letter2idx[letter][1]-cur_j
            # always move left and up before right and down
            # so that we never go out of board at the row z is in
            if d_i < 0: ret.extend(['U']*(-d_i))
            if d_j < 0: ret.extend(['L']*(-d_j))
            if d_i > 0: ret.extend(['D']*d_i)
            if d_j > 0: ret.extend(['R']*d_j)
            ret.append('!')
            cur_i, cur_j = letter2idx[letter]

        return "".join(ret)