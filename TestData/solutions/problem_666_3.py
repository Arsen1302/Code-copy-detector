class Solution:
    def solution_666_3(self, a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
        ans = []
        i, j = 0, 0
        
        while i < len(a) and j < len(b):
            ai, aj = a[i]
            bi, bj = b[j]
            
            if bj >= ai and aj >= bi:
                ans.append([max(ai, bi), min(aj, bj)])
            
            if bj >= aj:
                i += 1
            else:
                j += 1
        
        return ans