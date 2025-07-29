class Solution:
    def solution_1018_3(self, s: str) -> int:
        cnt, ans = 0, 0
        for i in range(len(s)):
            if s[i] == '0':
                cnt = 0
            else:
                cnt += 1
                ans += cnt
        return ans % ((10**9)+7)