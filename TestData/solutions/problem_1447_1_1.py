class Solution:
    def solution_1447_1_1(self, arr: List[int], k: int) -> int:
        
        def solution_1447_1_2(sub): 
            """Return ops to make sub non-decreasing."""
            vals = []
            for x in sub: 
                k = bisect_right(vals, x)
                if k == len(vals): vals.append(x)
                else: vals[k] = x
            return len(sub) - len(vals)
        
        return sum(solution_1447_1_2(arr[i:len(arr):k]) for i in range(k))