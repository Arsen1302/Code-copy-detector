class Solution:
    def solution_1195_5_1(self, nums: List[int], maxOperations: int) -> int:
        l = 1
        r = max(nums)
        
        while l < r:
            mid = l + (r-l) // 2
            solution_1195_5_2 = self.solution_1195_5_2(mid,nums)
            if solution_1195_5_2 <= maxOperations:
                r = mid
            else:
                l = mid+1
        return r  # or l
    
    
    def solution_1195_5_2(self,n,arr):
        return sum((a-1) // n for a in arr)