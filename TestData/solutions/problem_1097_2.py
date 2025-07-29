class Solution:
    def solution_1097_2(self, s: str) -> int:
        ans = [-1]
        
        for i in set(s):
            if(s.count(i) >= 2):
                ans.append(s.rindex(i) - s.index(i) - 1 )
        
        return max(ans)