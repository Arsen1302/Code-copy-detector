class Solution:
    def solution_1514_4(self, nums: List[int], key: int, k: int) -> List[int]:
        ans = []
        ii = 0
        for i, x in enumerate(nums): 
            if x == key: 
                lo, hi = max(ii, i-k), min(i+k+1, len(nums))
                ans.extend(list(range(lo, hi)))
                ii = hi
        return ans