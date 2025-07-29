class Solution:
    def solution_1482_4(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        n = len(s)
        if n == k: return s
        l = 0
        val = 0
        mapp = pow(power,k-1, modulo) 
        s = s[::-1]
        for i in range(k):
            val+= ( (ord(s[i]) - ord('a') + 1) * pow(power,k-1 - i, modulo)  )  % modulo
        val = val % modulo
        res = []
        for i in range(k, n):
            if i - l >= k:
                if val % modulo == hashValue:
                    res.append( (l,i))
                val = ( val  - ((ord(s[l])-ord('a') + 1) * mapp) % modulo  + modulo)  % modulo
                val = (val*power) % modulo
                l+=1
            val+= (ord(s[i]) - ord('a') + 1) 
            val = val % modulo
        if val == hashValue:
            res.append( (l,n) )
        return s[ res[-1][0]: res[-1][1] ][::-1]
	```