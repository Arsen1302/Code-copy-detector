class Solution:
    def solution_869_2(self, a: int, b: int, c: int) -> int:
        a, b, c, t, D = bin(a)[2:], bin(b)[2:], bin(c)[2:], 0, {'010':1, '100':1, '001':1, '110':2}
        M = max(len(a),len(b),len(c))
        a, b, c = a.zfill(M), b.zfill(M), c.zfill(M)
        for i in range(M): t += D.get(a[i]+b[i]+c[i],0)
        return t
		
		
- Junaid Mansuri
- Chicago, IL