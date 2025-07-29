class Solution:
    def solution_721_4(self, n: int, p: List[List[int]]) -> List[int]:
    	G, B, A = [set([1,2,3,4]) for i in range(n)], [[] for i in range(n)], []
    	for i in p: B[i[0]-1].append(i[1]), B[i[1]-1].append(i[0])
    	for i in range(n):
    		A.append(G[i].pop())
    		for j in B[i]: G[j-1].discard(A[i])
    	return A
		
		
- Junaid Mansuri
(LeetCode ID)@hotmail.com