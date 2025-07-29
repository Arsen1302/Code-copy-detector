class Solution:
    def solution_376_3(self, dict: List[str], sentence: str) -> str:
    	D, s = {}, sentence.split()
    	for d in dict:
    		if d[0] in D: D[d[0]].append([d,len(d)])
    		else: D[d[0]] = [[d,len(d)]]
    	for i in D: D[i].sort(key = lambda x: x[1])
    	for i,j in enumerate(s):
    		f, t = j[0], len(j)
    		if f not in D: continue
    		for a,b in D[f]:
    			if b > t: break
    			if a == j[:b]:
    				s[i] = a
    				break
    	return " ".join(s) 
		
		
- Junaid Mansuri
(LeetCode ID)@hotmail.com