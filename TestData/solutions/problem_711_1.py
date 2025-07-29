class Solution:
    def solution_711_1(self, A: List[int], L: int, M: int) -> int:
        prefix = [0]
        for x in A: prefix.append(prefix[-1] + x) # prefix sum w/ leading 0
        ans = lmx = mmx = -inf 
        for i in range(M+L, len(A)+1): 
            lmx = max(lmx, prefix[i-M] - prefix[i-L-M])
            mmx = max(mmx, prefix[i-L] - prefix[i-L-M])
            ans = max(ans, lmx + prefix[i] - prefix[i-M], mmx + prefix[i] - prefix[i-L])
        return ans