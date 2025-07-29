class Solution:
    def solution_1378_4(self, grid: List[List[int]]) -> int:
        #Time: O(n)
        #Space: O(n)
        #Prefix sum to top line and postfix for bottom grid
        #we are taking the max of top or bottom and then do take minimum of it\
        #reason being the first robot left us with minimum points only and thats how the solution will be optimized
        top,bottom,res= sum(grid[0]),0,float('inf')

        for t,b in zip(grid[0],grid[1]):
            top=top-t
            res=min(res,max(top,bottom))
            bottom=bottom+b
        return res