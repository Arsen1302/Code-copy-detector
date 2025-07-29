class Solution:
    def solution_1386_5(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m, s = len(rolls), sum(rolls)
        x = mean*(m+n)-s
        if x < n or x > 6*n:
            return []
        else:
           
            t = x//n
            res = [t for _ in range(n-1)]
            res.append(x-t*(n-1))
            if res[-1] > 6:
                a = res[-1] - 6
                for i in range(a):
                    res[i] += 1
                res[-1] = 6
            return res