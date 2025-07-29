class Solution:
    def solution_679_3_1(self, board: List[List[str]]) -> int:
        
        def solution_679_3_2(rx, ry, direction, count):
            if rx == 8 or ry == 8 or rx == -1 or ry == -1: return count
            if board[rx][ry] == "B": return 0
            if board[rx][ry] == "p": return count + 1
            if direction == "L": return solution_679_3_2(rx, ry - 1, "L", count)
            elif direction == "R": return solution_679_3_2(rx, ry + 1, "R", count)
            elif direction == "U": return solution_679_3_2(rx - 1, ry, "U", count)
            else: return solution_679_3_2(rx + 1, ry, "D", count)
            
        rookx = rooky = -1
        for i in range(len(board)):
            if "R" in board[i]:
                rookx, rooky = i, board[i].index("R")
                break
                
        return solution_679_3_2(rookx, rooky, "L", 0) + solution_679_3_2(rookx, rooky, "R", 0) + solution_679_3_2(rookx, rooky, "U", 0) + solution_679_3_2(rookx, rooky, "D", 0)