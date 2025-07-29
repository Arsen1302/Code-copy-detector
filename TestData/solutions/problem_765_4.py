class Solution:
    def solution_765_4(self, target: str) -> str:
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        
        # greedy because starting from 0,0 no matter
        # the next letter the best move is always just going
        # directly to it in terms of distance between
        # prev - cur
        coords = {}
        pc = "a"
        
        for row in range(len(board)):
            for col in range(len(board[row])):
                # col = x, row = y
                coords[board[row][col]] = (row, col)
        
        moves = []

        # how to account for z??
        # you know its z and special if its row 5
        # and col is != 0
        for nc in target:
            # get diff which represents the amount to move
            # from the cur x,y coordinate
            cur = coords[pc]
            nxt = coords[nc]
            r_cur, c_cur = cur
            r_nxt, c_nxt = nxt
            r_diff = r_nxt - r_cur
            c_diff = c_nxt - c_cur
            
            # where char = z and then the column to move from
            # is not 0 then you need to go left then go down
            # otherwise if 0 you cna just follow normal
            if nc == "z" and c_cur != 0:
                # this is special z case, just go left to pin
                # to LHS then go down
                moves.append("L" * abs(c_diff))
                moves.append("D" * abs(r_diff))
            else:
                if r_diff > 0:
                    moves.append("D" * r_diff)
                else:
                    moves.append("U" * abs(r_diff))

                if c_diff > 0:
                    moves.append("R" * c_diff)
                else:
                    moves.append("L" * abs(c_diff))
            
            # mark and add char
            moves.append("!")
            
            # make new previous to current
            pc = nc
        
        return "".join(moves)