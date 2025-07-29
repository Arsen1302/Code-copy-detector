class Solution:
    def solution_500_2_1(self, p: List[List[int]]) -> float:
        L, A = len(p), 0
        for i in range(L-2):
        	for j in range(i+1,L-1):
        		for k in range(j+1,L):
        			R = solution_500_2_2(p[i],p[j],p[k])
        			A = max(A,R)
        return A

def solution_500_2_2(a,b,c):
	return abs(a[0]*b[1]+b[0]*c[1]+c[0]*a[1]-(a[0]*c[1]+c[0]*b[1]+b[0]*a[1]))/2