class Solution:
    def solution_283_2_1(self, nums: List[int]) -> int:
        
        def solution_283_2_2(nums, aux, lo, hi): 
            """Return number of reverse pairs in nums[lo:hi]."""
            if lo + 1 == hi: return 0 
            mid = lo + hi >> 1
            left = solution_283_2_2(aux, nums, lo, mid)
            right = solution_283_2_2(aux, nums, mid, hi)
            split = 0 
            i, j = lo, mid
            for _ in range(lo, hi): 
                if i == mid or j < hi and aux[i] > 2*aux[j]: 
                    split += mid - i 
                    j += 1
                else: i += 1
            i, j = lo, mid
            for k in range(lo, hi): 
                if j == hi or i < mid and aux[i] < aux[j]: 
                    nums[k] = aux[i]
                    i += 1
                else: 
                    nums[k] = aux[j]
                    j += 1
            return left + split + right 
                
        return solution_283_2_2(nums, nums.copy(), 0, len(nums))