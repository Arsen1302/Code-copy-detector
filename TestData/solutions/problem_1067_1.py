class Solution:
    def solution_1067_1(self, s: str, cost: List[int]) -> int:
        ans = prev = 0 # index of previously retained letter 
        for i in range(1, len(s)): 
            if s[prev] != s[i]: prev = i
            else: 
                ans += min(cost[prev], cost[i])
                if cost[prev] < cost[i]: prev = i
        return ans