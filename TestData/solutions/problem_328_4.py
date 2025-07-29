class Solution:
    def solution_328_4(self, W: List[List[int]]) -> int:
    	L, C = len(W), collections.Counter(sum([list(itertools.accumulate(w)) for w in W],[]))
    	C[sum(W[0])] = 0
    	return L - max(C.values())
		
		
- Junaid Mansuri
(LeetCode ID)@hotmail.com