class Solution:
    def solution_1590_4(self, l: List[List[int]], k: int) -> float:
        prev=sol=0
        for x,y in l:
            t, prev = min(x,k)-prev, x
            if t<0:break
            sol+=t*y/100
        return sol