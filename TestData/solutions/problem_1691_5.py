class Solution:
    def solution_1691_5(self, n: int, queries: List[List[int]]) -> List[int]:
        powersOf2 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824]
        
        p = []
        ans = []
        MOD = 10**9+7
        
        while n > 0:
            idx = bisect_left(powersOf2, n)
            if idx and powersOf2[idx] != n:
                idx -= 1
            p.append(powersOf2[idx])
            n -= powersOf2[idx]
            
        p = p[::-1]
        
        for i in range(1, len(p)):
            p[i] *= p[i-1]

        for l, r in queries:
            if l: 
                ans.append((p[r]//p[l-1])%MOD)
            else:
                ans.append(p[r]%MOD)
        return ans