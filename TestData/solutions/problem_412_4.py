class Solution:
    def solution_412_4(self, s: str) -> int:
    	L = len(s)
    	a = [-1]+[i for i in range(L-1) if s[i] != s[i+1]]+[L-1]
    	b = [a[i]-a[i-1] for i in range(1,len(a))]
    	c = [min(b[i-1],b[i]) for i in range(1,len(b))]
    	return sum(c)