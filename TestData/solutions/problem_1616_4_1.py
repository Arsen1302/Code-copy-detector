class Solution:
    def solution_1616_4_1(self, m: int, n: int) -> int:
        def solution_1616_4_2(num):
            i = 2
            ct = Counter()
            while i <= num//i:
                if num % i == 0:
                    j = 0
                    while num % i == 0:
                        num //= i
                        j += 1
                    ct[i] = j
                i += 1
            if num!=1:
                ct[num] += 1
            return ct
        mod = 10**9 + 7
        res = 1
        for i in range(2,n+1):
            ctr = solution_1616_4_2(i)
            p = 1
            for key in ctr:
                ct = ctr[key]
                p = (p * comb(m+ct-1, m-1)) % mod
            res = (res + p) % mod
        return res