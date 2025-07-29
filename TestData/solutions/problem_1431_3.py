class Solution:
    def solution_1431_3(self, nums: List[int]) -> int:
        min_i = max_i = None
        min_num, max_num = math.inf, -math.inf
        for i, num in enumerate(nums):
            if num < min_num:
                min_i, min_num = i, num
            if num > max_num:
                max_i, max_num = i, num
       
        if min_i > max_i:
            min_i, max_i = max_i, min_i
		
        n = len(nums)
        
        return min(min_i + 1 + n - max_i,  # delete from left and right
                   max_i + 1,  # delete from left only
                   n - min_i)  # delete from right only