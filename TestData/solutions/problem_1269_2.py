class Solution:
    def solution_1269_2(self, nums: List[int]) -> int:
        ans = 0 
        for x in nums: 
            ans |= x 
        return ans * 2 ** (len(nums)-1)