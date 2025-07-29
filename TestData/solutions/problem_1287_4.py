class Solution:
    def solution_1287_4(self, s: str) -> int:
        s = [int(x) for x in s]
        ans = inf
        x01 = x10 = 0 
        for i in range(2*len(s)): 
            x01 += s[i%len(s)]^i&amp;1
            x10 += s[i%len(s)]^(i+1)&amp;1
            if i+1 >= len(s): 
                if i >= len(s):
                    x01 -= s[i-len(s)]^(i-len(s))&amp;1
                    x10 -= s[i-len(s)]^(i-len(s)+1)&amp;1
                ans = min(ans, x01, x10)
        return ans