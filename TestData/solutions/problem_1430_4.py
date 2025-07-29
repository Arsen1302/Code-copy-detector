class Solution:
    def solution_1430_4(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        t=2*k+1
        if n<t:
            return [-1]*n
        ans=[-1]*k
        s=sum(nums[:t])
        avg=s//t
        ans.append(avg)
        l,r=0,t
        for i in range(k+1,n):
            if i+k>=n:
                ans.append(-1)
            else:
                s+=nums[r]-nums[l]
                avg=s//t
                ans.append(avg)
            l+=1
            r+=1
        return ans