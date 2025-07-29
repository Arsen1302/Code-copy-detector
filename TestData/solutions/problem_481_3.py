class Solution:
    def solution_481_3(self, order: str, s: str) -> str:
        ans = ""
        for ch in order:
            cnt = s.count(ch)
            for i in range(cnt):
                ans += ch
        
        for ch in s:
            if ch not in order:
                ans += ch
        
        return ans