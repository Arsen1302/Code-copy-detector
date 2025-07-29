class Solution:
    def solution_1566_3(self, nums: List[int]) -> int:
        c=0
        s=sum(nums)
        k=0
        for i in range(len(nums)-1):
            s=s-nums[i]
            c+=nums[i]
            if s<=c:
                k+=1
        return k