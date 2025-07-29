class Solution:
    def solution_308_5(self, nums: List[int], k: int) -> bool:
        # ////// TC O(N) //////
        remainder = { 0 : -1} # mapping remainder with last index 
        total = 0
        
        for i,n in enumerate(nums):
            total += n
            rem = total % k
            if rem not in remainder:
                remainder[rem] = i
            elif i - remainder[rem] > 1: # making sure that the subarray is of at least of len 2
                return True
        return False