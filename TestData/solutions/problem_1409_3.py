class Solution:
def solution_1409_3(self, nums: List[int], start: int, goal: int) -> int:
    if start==goal:
        return 0
    
    q = [(start,0)]
    seen = {start}
    while q:
        n,s = q.pop(0)
        for num in nums:
            for cand in [n+num,n-num,n^num]:
                if cand==goal:
                    return s+1
                if 0<=cand<=1000 and cand not in seen:
                    seen.add(cand)
                    q.append((cand,s+1))
    
    return -1