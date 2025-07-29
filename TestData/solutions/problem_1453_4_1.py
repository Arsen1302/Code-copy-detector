class Solution:
    def solution_1453_4_1(self, n: int, startPos: List[int], s: str) -> List[int]:
        
        @cache
        def solution_1453_4_2(i, j, k): 
            """Return valid number of instructions at (i, j) starting from kth."""
            if k == len(s): return 0 
            if s[k] == 'L': j -= 1
            elif s[k] == 'R': j += 1
            elif s[k] == 'U': i -= 1
            else: i += 1
            if 0 <= i < n and 0 <= j < n: return 1 + solution_1453_4_2(i, j, k+1)
            return 0 
        
        return [solution_1453_4_2(*startPos, k) for k in range(len(s))]