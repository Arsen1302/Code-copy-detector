class Solution:
    def solution_1632_3(self, nums: List[int]) -> int:
        count=0
        n=len(nums)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if j-i!=nums[j]-nums[i]:
        #             count+=1
        # return count
        d={}
        for i in range(n):
            if nums[i]-i in d:
                count+=d[nums[i]-i]
                d[nums[i]-i]+=1
            else:
                d[nums[i]-i]=1

        return (n*(n-1)//2) - count