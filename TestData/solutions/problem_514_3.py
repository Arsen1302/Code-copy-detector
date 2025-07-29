class Solution:
    def solution_514_3(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        mp = {}
        mx = 0
        for x, y in sorted(zip(difficulty, profit)):
            mp[x] = max(mp.get(x, 0), mx := max(mx, y))
        arr = list(mp.keys()) # ordered since 3.6
        
        ans = 0 
        for x in worker: 
            i = bisect_right(arr, x) - 1
            if 0 <= i < len(arr): ans += mp[arr[i]]
        return ans