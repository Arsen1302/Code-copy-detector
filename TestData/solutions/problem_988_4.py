class Solution:
    def solution_988_4(self, nums: List[int], n: int) -> List[int]:
        c=[]
        for i in range(n):
            c.append(nums[i])
            c.append(nums[n+i])
        return c