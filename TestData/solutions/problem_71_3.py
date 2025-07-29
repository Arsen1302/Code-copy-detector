class Solution:
    def solution_71_3(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        m=0
        for i in range(n-1):
            m=max(m,abs(nums[i]-nums[i+1]))
        return m