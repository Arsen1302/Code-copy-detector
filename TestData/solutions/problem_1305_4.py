class Solution:
    def solution_1305_4(self, nums: List[int]) -> int:
        m,n= max(nums),min(nums)
        nums.remove(m)
        nums.remove(n)
        return (m*max(nums)) - (n*min(nums))