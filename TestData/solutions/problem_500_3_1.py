class Solution:
    def solution_500_3_1(self, p: List[List[int]]) -> float:
        L, A = len(p), 0
        for i in range(L-2):
        	for j in range(i+1,L-1):
        		for k in range(j+1,L):
        			R = solution_500_3_2(p[i],p[j],p[k])
        			A = max(A,R)
        return A

def solution_500_3_2(r,s,t):
	a, b, c = math.hypot(r[0]-s[0],r[1]-s[1]), math.hypot(r[0]-t[0],r[1]-t[1]), math.hypot(s[0]-t[0],s[1]-t[1])
	s = (a + b + c)/2
	return (max(0,s*(s-a)*(s-b)*(s-c)))**.5



- Junaid Mansuri
(LeetCode ID)@hotmail.com