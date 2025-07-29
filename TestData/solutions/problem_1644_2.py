class Solution:
    def solution_1644_2(self, s: str) -> int:

        ans = 0

        while '01' in s:
            ans += 1
            s = s.replace('01', '10')
            
        return ans