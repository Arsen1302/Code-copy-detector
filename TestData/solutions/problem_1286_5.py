class Solution:
    def solution_1286_5(self, nums: List[int]) -> int:
        # Let's re-interpret this question 
        # --> for each value, we would like to sum-up values smaller than itself (without double count)
        # e.g., [5, 1, 3]
        # 5 is larger than 1, 3 --> 2
        # 1 is the smallest     --> 0
        # 3 is larger than 1    --> 1 
        # ------------------------------------------------------------
        # When we iterate value in the loop, 
        # we want to quickly know how many smaller values compared to certain given value  
        # --> we would sort array &amp; build a dictionary for this
        # ------------------------------------------------------------
        # Time Complexity: O(n*log(n))
        
        uniq_nums = list(set(nums))
        uniq_sorted_nums = sorted(uniq_nums)
        
        #i stands for index, but here it also presents number of unique values smaller than current value 
        d = {v: i for i, v in enumerate(uniq_sorted_nums)}
        
        return sum([d[num] for num in nums])