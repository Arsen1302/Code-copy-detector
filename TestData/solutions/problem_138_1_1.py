class Solution:
    def solution_138_1_1(self, n: int) -> bool:
        sq = int(math.sqrt(n))
        return sq*sq == n
        
    def solution_138_1_2(self, n: int) -> int:
        # Lagrange's four-square theorem
        if self.solution_138_1_1(n):
            return 1
        while (n &amp; 3) == 0:
            n >>= 2
        if (n &amp; 7) == 7:
            return 4
        sq = int(math.sqrt(n)) + 1
        for i in range(1,sq):
            if self.solution_138_1_1(n - i*i):
                return 2
        return 3