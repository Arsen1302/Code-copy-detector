class Solution:
    def solution_547_5(self, b: List[int]) -> bool:
    	L, B = len(b), {5:0, 10:0, 20:0}
    	for i in range(L):
    		if b[i] == 10:
    			if B[5] == 0: return False
    			else: B[5] -= 1
    		elif b[i] == 20:
    			if B[10] != 0 and B[5] != 0: B[5], B[10] = B[5] - 1, B[10] - 1
    			elif B[5] >= 3: B[5] -= 3
    			else: return False
    		B[b[i]] += 1
    	return True
		
		
- Junaid Mansuri
(LeetCode ID)@hotmail.com