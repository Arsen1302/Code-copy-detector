class Solution:
    def solution_1472_5(self, cost: List[int]) -> int:
        cost.sort()
        cost = cost[::-1]
        ans = 0
        n = len(cost)
        for i in range(n):
            if (i+1)%3!=0:
                ans += cost[i] 
        return ans