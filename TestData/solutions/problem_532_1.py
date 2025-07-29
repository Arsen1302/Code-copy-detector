class Solution:
    def solution_532_1(self, S: str, T: str) -> bool:
    	a, A = [collections.deque(), collections.deque()], [S,T]
    	for i in range(2):
	    	for j in A[i]:
   		 		if j != '#': a[i].append(j)
   		 		elif a[i]: a[i].pop()
    	return a[0] == a[1]