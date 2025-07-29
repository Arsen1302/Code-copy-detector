class Solution:
    def solution_222_5(self, nums: List[int]) -> int:
        length=len(nums)
        res=0
        if length>=3:
            count=0
            for i in range(length-2):
                if nums[i]-nums[i+1]==nums[i+1]-nums[i+2]:
                    count+=1
                    res+=count
                else:
                    count=0
        return res