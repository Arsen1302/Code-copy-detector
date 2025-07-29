class Solution:
    def solution_895_3_1(self, grid: List[List[int]]) -> int:
        
        def solution_895_3_2(row):
            l,h=0,len(row)
            while (l<h):
                m=(l+h)//2
                if (row[m] <0):
                    h=m
                elif (g[m]>=0):
                    l=m+1
            return len(row)-h
        
        count=0
        for g in grid:
            print(solution_895_3_2(g))
            count=count+solution_895_3_2(g)
        return count