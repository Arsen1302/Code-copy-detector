class Solution:
    def solution_329_5(self, n: int) -> int:
        d = {}
        n = list(str(n))
        k = len(n) - 1
        while(k >= 0 ):
            value = int(n[k])
            for j in range(value+1, 10):
                if(j in d):
                    n[k], n[d[j]] = str(n[d[j]]), n[k]
                    a = int(''.join(n[:k+1]) + ''.join(sorted(n[k+1 : ])))
                    return a if a < 1<<31 else -1
            if(value not in d):
                d[value] = k
            k -= 1
        return -1