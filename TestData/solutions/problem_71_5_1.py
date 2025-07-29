class Solution:
    def solution_71_5_1(self,arr,n):
        max_ele=max(arr)
        size=max_ele/n
        bucketList=[[] for i in range(n)]
        for i in range(n):
            j=int(arr[i]/size)
            if j==n:bucketList[j-1].append(arr[i])
            else:bucketList[j].append(arr[i])
        for i in bucketList:
            if i:i.sort()
        k=0
        for lst in bucketList:
            if lst:
                for i in lst:
                    arr[k]=i
                    k+=1
    def solution_71_5_2(self, nums: List[int]) -> int:
        n=len(nums)
        if n<2:return 0
        self.solution_71_5_1(nums,n)
        ans=0
        for i in range(n-1):
            x=nums[i+1]-nums[i]
            if x>ans:ans=x
        return ans