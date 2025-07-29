class Solution:
    def solution_1515_5(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        dig = {(x, y) for x, y in dig}
        ans = 0 
        for i1, j1, i2, j2 in artifacts: 
            for i in range(i1, i2+1):
                for j in range(j1, j2+1): 
                    if (i, j) not in dig: break 
                else: continue 
                break 
            else: ans += 1
        return ans