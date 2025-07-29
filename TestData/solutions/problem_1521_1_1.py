class Solution:
    def solution_1521_1_1(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        
        @cache
        def solution_1521_1_2(i, n):
            """Return min while tiles at k with n carpets left."""
            if n < 0: return inf 
            if i >= len(floor): return 0 
            if floor[i] == '1': return min(solution_1521_1_2(i+carpetLen, n-1), 1 + solution_1521_1_2(i+1, n))
            return solution_1521_1_2(i+1, n)
        
        return solution_1521_1_2(0, numCarpets)