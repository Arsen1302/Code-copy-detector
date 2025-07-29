class Solution:
    def solution_557_5(self, A: List[int], B: List[int]) -> List[int]:
        A.sort()
        mp = {}
        for x in sorted(B, reverse=True): 
            if x < A[-1]: mp.setdefault(x, []).append(A.pop())
        
        ans = []
        for x in B: 
            if x in mp and mp[x]: 
                ans.append(mp[x].pop())
            else: 
                ans.append(A.pop())
        return ans