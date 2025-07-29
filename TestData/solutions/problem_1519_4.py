class Solution:
    def solution_1519_4(self, text: str, pattern: str) -> int:
        ans = cnt0 = cnt1 = 0 
        for ch in text: 
            if ch == pattern[1]: 
                ans += cnt0 
                cnt1 += 1
            if ch == pattern[0]: cnt0 += 1
        return ans + max(cnt0, cnt1)