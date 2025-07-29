class Solution:
    def solution_499_3(self, cpdomains: List[str]) -> List[str]:
    	D = {}
    	for c in cpdomains:
    		s = c.replace('.',' ').split()
    		n = int(s[0])
    		for i in range(len(s)-1,0,-1):
    			t = ".".join(s[i:])
    			D[t] = D[t] + n if t in D else n
    	return [str(D[i])+" "+i for i in D]
		
		
- Junaid Mansuri