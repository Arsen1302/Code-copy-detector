class Solution:
    def solution_442_1_1(self, nums: List[int]) -> int:
        mp = {}
        for x in nums: mp[x] = x + mp.get(x, 0)
        
        @lru_cache(None)
        def solution_442_1_2(i): 
            """Return maximum points one can earn from nums[i:]."""
            if i >= len(nums): return 0 
            if nums[i] + 1 not in mp: return mp[nums[i]] + solution_442_1_2(i+1)
            return max(mp[nums[i]] + solution_442_1_2(i+2), solution_442_1_2(i+1))
        
        nums = sorted(set(nums))
        return solution_442_1_2(0)