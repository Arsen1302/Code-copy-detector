class Solution:
    def solution_462_3(self, arr: List[int]) -> int:
        mn = [inf]*(1 + len(arr))
        for i in reversed(range(len(arr))): mn[i] = min(arr[i], mn[i+1])
        
        ans = mx = 0 
        for i, x in enumerate(arr): 
            mx = max(mx, x)
            if mx <= mn[i+1]: ans += 1
        return ans