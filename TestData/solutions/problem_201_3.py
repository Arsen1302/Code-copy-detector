class Solution:
    def solution_201_3(self, n: int) -> int:
        i, di = 0, 2
        for _ in range(n-1): 
            if not 0 <= i+di < n: 
                i += di//2 if 0 <= i + di//2 < n else -di//2
                di *= -2 
            else: i += di 
        return i+1