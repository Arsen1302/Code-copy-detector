class Solution:
    def solution_1721_5(self, s: str, k: int) -> int:
        ans = 0
        l = 0
        while l<len(s):
            cdd1 = s[l:l+k]
            if len(cdd1)>=k and cdd1 == cdd1[::-1]:
                ans += 1
                l = l+k
                continue
            cdd2 = s[l:l+k+1]
            if len(cdd2)>=k and cdd2 == cdd2[::-1]:
                ans += 1
                l = l+k+1
                continue
            l += 1
        return ans