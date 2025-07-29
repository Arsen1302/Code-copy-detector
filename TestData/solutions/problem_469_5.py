class Solution:
    def solution_469_5(self, n: int, k: int) -> int:
        if n == 1:
            return 0

        if k % 2 == 0:
            parent = self.solution_469_5(n-1, k/2)
            if parent == 0:
                return 1
            else:
                return 0

        if k % 2 == 1
            parent = self.solution_469_5(n-1, (k+1)/2)
            if parent == 0:
                return 0
            else:
                return 1