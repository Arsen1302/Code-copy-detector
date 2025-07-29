class Solution:
    def solution_406_1_1(self, nums: List[int], k: int) -> List[int]:
        prefix = [0]
        for x in nums: prefix.append(prefix[-1] + x)
        
        @cache
        def solution_406_1_2(i, n): 
            """Return max sum of 3 non-overlapping subarrays."""
            if n == 0: return []
            if i+k >= len(prefix): return []
            return max([i] + solution_406_1_2(i+k, n-1), solution_406_1_2(i+1, n), key=lambda x: sum(prefix[xx+k] - prefix[xx] for xx in x))
        
        return solution_406_1_2(0, 3)