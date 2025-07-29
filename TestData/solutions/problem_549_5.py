class Solution:
    def solution_549_5(self, A: List[int], K: int) -> int:
    	C, m, a = [0]+list(itertools.accumulate(A)), float('inf'), collections.deque()
    	for i, c in enumerate(C):
    		while a and C[a[-1]] >= c: a.pop()
    		while a and c - C[a[0]] >= K: m = min(m, i - a.popleft())
    		a.append(i)
    	return -1 if m == float('inf') else m
		
		
- Junaid Mansuri
(LeetCode ID)@hotmail.com