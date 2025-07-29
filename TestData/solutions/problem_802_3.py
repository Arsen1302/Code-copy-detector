class Solution:
    def solution_802_3(self, arr: List[int], difference: int) -> int:
        d, ans = collections.defaultdict(int), 0
        for num in arr:
            d[num] = d[num-difference] + 1
            ans = max(ans, d[num])    
        return ans