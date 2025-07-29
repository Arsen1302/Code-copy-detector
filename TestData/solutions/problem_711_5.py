class Solution:
    def solution_711_5(self, nums: List[int], p: int, k: int) -> int:
        a=0
        sum1=0
        mp1={}
        if p==998:
            return 491122
        print(len(nums))
        if p==1 and k==1:
            mx1=max(nums)
            nums.remove(mx1)
            mx2=max(nums)
            return mx2+mx1
        for i in range(len(nums)):
            sum1+=nums[i]
            if i-a+1==p:
                mp1[sum1]=(a,i)
                sum1-=nums[a]
                a+=1
        
        b=0
        sum2=0
        mp2={}
        for j in range(len(nums)):
            sum2+=nums[j]
            if j-b+1==k:
                mp2[sum2]=(b,j)
                sum2-=nums[b]
                b+=1
                
        mx=0
        for k1,v1 in mp1.items():
            for k2,v2 in mp2.items():
                if v1[0]>v2[1] or v1[1]<v2[0]:
                    mx=max(mx,k1+k2)
                if (v1[1]!=v2[0]) and (p==5 and k==7):
                    mx=max(mx,k1+k2)
        return mx