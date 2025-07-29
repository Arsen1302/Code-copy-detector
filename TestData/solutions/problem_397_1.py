class Solution:
    def solution_397_1(self, nums: List[int]) -> int:
        counter=1
        temp=1
        for i in range(0,len(nums)-1):
            if nums[i]<nums[i+1]:
                temp+=1
                if temp>counter:
                    counter=temp
            else:
                temp=1
        return counter