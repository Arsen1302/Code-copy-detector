class Solution:
    def solution_1431_4(self, nums: List[int]) -> int:
        
        front_idx_maxi = nums.index(max(nums))
        front_idx_mini = nums.index(min(nums))
        
        n = len(nums)
                        
        li = sorted([front_idx_maxi,front_idx_mini])
        
        return min(li[1]+1,n-li[0],(li[0]+1)+(n-li[1]))