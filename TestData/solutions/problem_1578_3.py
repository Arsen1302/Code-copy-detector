class Solution:
    def solution_1578_3(self, n: int, roads: List[List[int]]) -> int:
        degrees = [0] * n  
        for x,y in roads:
            degrees[x] += 1 
            degrees[y] += 1
        degrees.sort()  # Cities with most roads would receive the most score        
        return sum(degrees[i] * (i+1) for i in range(len(degrees)))