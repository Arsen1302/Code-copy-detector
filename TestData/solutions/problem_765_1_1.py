class Solution:
    def solution_765_1_1(self):
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        self.d = {c:(i, j) for i, row in enumerate(board) for j, c in enumerate(row)}
                
    def solution_765_1_2(self, target: str) -> str:
        ans, prev = '', (0, 0)
        for c in target:
            cur = self.d[c]
            delta_x, delta_y = cur[0]-prev[0], cur[1]-prev[1]
            h = 'R'*delta_y if delta_y > 0 else 'L'*(-delta_y)                    
            v = 'D'*delta_x if delta_x > 0 else 'U'*(-delta_x)                    
            ans += (h+v if cur == (5,0) else v+h) + '!'
            prev = cur
        return ans