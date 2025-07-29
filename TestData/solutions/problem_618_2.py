class Solution:
    def solution_618_2(self, G: List[str]) -> List[str]:
    	A, B, G = [], [], [i.split() for i in G]
    	for g in G:
    		if g[1].isnumeric(): B.append(g)
    		else: A.append(g)
    	return [" ".join(i) for i in sorted(A, key = lambda x: x[1:]+[x[0]]) + B]
		
		
- Junaid Mansuri
(LeetCode ID)@hotmail.com