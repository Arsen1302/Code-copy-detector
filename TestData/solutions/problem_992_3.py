class Solution:
    def solution_992_3(self, arr: List[int], target: int) -> int:
        ans = inf 
        best = [inf]*len(arr) # shortest subarray ending at i
        prefix = 0
        latest = {0: -1}
        for i, x in enumerate(arr): 
            prefix += x
            if prefix - target in latest: 
                ii = latest[prefix - target]
                if ii >= 0: 
                    ans = min(ans, i - ii + best[ii])
                best[i] = i - ii
            if i: best[i] = min(best[i-1], best[i])
            latest[prefix] = i 
        return ans if ans < inf else -1