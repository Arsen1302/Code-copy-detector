class Solution:
    def solution_242_3(self, n: int, row=1) -> int:
        if n < row:
            return 0
        
        return 1 + self.solution_242_3(n - row, row + 1)