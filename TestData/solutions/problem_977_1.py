class Solution:
    def solution_977_1(self, s: str, k: int) -> int:
        x = 0
        for i in range(k):
            if s[i] in ('a', 'e', 'i', 'o', 'u'):
                x += 1
        ans = x
        for i in range(k,len(s)):
            if s[i] in ('a', 'e', 'i', 'o', 'u'):
                x += 1
            if s[i-k] in ('a', 'e', 'i', 'o', 'u'):
                x -= 1
            ans = max(ans,x)
        return ans