class Solution:
    def solution_555_5(self, n: int) -> int:
        l = []
        ans = 0
        s = bin(n)[2:]
        for i in range(len(s)):
            if s[i] == '1':
                l.append(i)
        if len(l)<=1:
            return 0
        if len(l)==2:
            return l[-1]-l[0]
        for i in range(1,len(l)):
            ans = max(ans, l[i]-l[i-1])
        return ans