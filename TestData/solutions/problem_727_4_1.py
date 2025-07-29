class Solution:
    def solution_727_4_1(self, stones: List[int]) -> int:
		# Divide the stones into two subsets
		# Find the min of the difference of two subsets
        total = sum(stones)
        max_subset_size = total / 2
        
		# _sum: the sum of the subsetA
		# cur_idx: current stone index
        @lru_cache(None)
        def solution_727_4_2(cur_idx, _sum):
			# diff = abs(subsetA - subsetB)
			#        = abs(_sum, total - _sum)
			#        = total - _sum - _sum
			#        = total - _sum * 2
            if cur_idx == len(stones):
                return total - _sum * 2
            
			# We can not put the stone to this subset. Therefore, we bypass this stone.
			# In other word, this stone is placed to another subset.
            if _sum + stones[cur_idx] > max_subset_size:
                return solution_727_4_2(cur_idx+1, _sum)
            
			# put the stone to current subset v.s bypass the stone 
            return min(solution_727_4_2(cur_idx+1, _sum), solution_727_4_2(cur_idx+1, _sum + stones[cur_idx]))
        
        return solution_727_4_2(0, 0)