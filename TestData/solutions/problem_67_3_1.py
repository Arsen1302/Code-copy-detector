class Solution:
    def solution_67_3_1(self, nums: List[int]) -> int:
        new=self.solution_67_3_3(nums)
        print(new)
        res=self.solution_67_3_2(new)
        return res
    def solution_67_3_2(self,nums):
        l,r,ans=0,len(nums)-1,nums[0]
        while l<=r:
            if nums[l]<nums[r]:
                ans=min(ans,nums[l])
                break
            mid=l+(r-l)//2
            ans=min(ans,nums[mid])
            if nums[mid]>=nums[l]:
                l=mid+1
            else:
                r=mid-1
        return ans
    def solution_67_3_3(self,items):
        list1 = []
        for i in items:
            if i not in list1:
                list1.append(i)
        return list1