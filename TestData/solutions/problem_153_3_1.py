class Solution:
    def solution_153_3_1(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        nums = list(enumerate(nums))
        
        def solution_153_3_2(nums, aux, lo, hi): 
            """Sort nums via merge sort and populate ans."""
            if lo+1 >= hi: return 
            mid = lo + hi >> 1
            solution_153_3_2(aux, nums, lo, mid)
            solution_153_3_2(aux, nums, mid, hi)
            i, j = lo, mid 
            for k in range(lo, hi): 
                if j >= hi or i < mid and aux[i][1] <= aux[j][1]: 
                    nums[k] = aux[i]
                    ans[nums[k][0]] += j - mid
                    i += 1
                else: 
                    nums[k] = aux[j]
                    j += 1
                    
        solution_153_3_2(nums, nums.copy(), 0, len(nums))
        return ans