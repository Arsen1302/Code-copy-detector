class Solution:
    def solution_1289_4(self, ranges: List[List[int]], left: int, right: int) -> bool:
        vals = [0]*52 
        for x, y in ranges: 
            vals[x] += 1
            vals[y+1] -= 1
        prefix = 0 
        for i, x in enumerate(vals): 
            prefix += x
            if left <= i <= right and prefix == 0: return False 
        return True