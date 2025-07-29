class Solution:
    def solution_73_5(self, n: int, d: int) -> str:
    	if n % d == 0: return str(n//d)
    	s, n, d, R, p = int(math.copysign(1,n*d)), abs(n), abs(d), {}, 2
    	A, (Q,n) = ['-'*(s < 0),str(n//d),'.'], divmod(n,d)
    	while 1:
    		(q,r) = divmod(n*10,d)
    		if n in R: return "".join(A[:R[n]]+['(']+A[R[n]:]+[')'])
    		R[n], n, p, _ = p + 1, r, p + 1, A.append(str(q))
    		if r == 0: return "".join(A)
			
			
- Junaid Mansuri
(LeetCode ID)@hotmail.com