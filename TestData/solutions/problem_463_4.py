class Solution:
    def solution_463_4(self, arr: List[int]) -> int:
        ans = prefix = 0
        for i, x in enumerate(arr): 
            prefix = max(prefix, x)
            if i == prefix: ans += 1
        return ans