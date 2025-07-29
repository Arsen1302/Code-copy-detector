class Solution:
    def solution_412_5(self, s: str) -> int:
    	return sum((lambda x: [min(x[i]-x[i-1],x[i+1]-x[i]) for i in range(1,len(x)-1)])([-1]+[i for i in range(len(s)-1) if s[i] != s[i+1]]+[len(s)-1]))
		
		
- Junaid Mansuri
(LeetCode ID)@hotmail.com