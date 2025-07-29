class Solution:
    def solution_791_2(self, arr: List[int], k: int) -> int:
        rsm = val = 0 
        sm = sum(arr)
        if k > 1: arr *= 2
        for x in arr: 
            val = max(0, val + x)
            rsm = max(rsm, val)
        return max(rsm, rsm + max(0, k-2)*sm) % 1_000_000_007