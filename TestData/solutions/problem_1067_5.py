class Solution:
def solution_1067_5(self, s: str, cost: List[int]) -> int:
    n = len(s)
    if n<2:
        return 0
    
	res, i = 0, 0
    for j in range(1,n):
        if s[i]==s[j]:
            res+=min(cost[i],cost[j])
            if cost[i]<cost[j]:
                i = j
        else:
            i = j
        
    return res