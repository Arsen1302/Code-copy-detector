class Solution:
    def solution_609_4(self, arr: List[int]) -> List[int]:
        MOD = 1_000_000_007
        total = 0 
        p2 = [1]
        for x in arr: 
            total = (2*total + x) % MOD 
            p2.append((p2[-1] << 1) % MOD)
        
        seen = {}
        prefix = 0
        for j, x in enumerate(arr): 
            prefix = (2*prefix + x) % MOD
            diff = (total - prefix * p2[len(arr)-1-j]) % MOD 
            if diff in seen:
                i = seen[diff]
                if diff == (prefix - diff * p2[j - i]) % MOD: return [i, j+1]
            seen[prefix] = j
        return [-1, -1]