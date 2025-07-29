class Solution:
    def solution_1492_5(self, beans: List[int]) -> int:
        beans.sort()
        n = len(beans)
        minSteps = float('inf')
        totalSum = 0
        
        for i in range(n):
            totalSum += beans[i]
            
        for i in range(n):
            newSum = totalSum-(n-i)*beans[i]
            minSteps = min(minSteps, newSum)
            
        return minSteps