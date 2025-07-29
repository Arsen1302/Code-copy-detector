class Solution:
    def solution_1473_5(self, differences: List[int], lower: int, upper: int) -> int:
        cum_sum = [0]
        for diff in differences:
            cum_sum.append(cum_sum[-1]+diff)
    
        max_diff = max(cum_sum)-min(cum_sum)
        
		if upper-lower < max_diff:
            return 0
        
		return upper-lower-max_diff+1