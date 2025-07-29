class Solution:
    def solution_1663_4(self, nums: List[int]) -> int:
        h={}
        for i in nums:
            if i%2==0:
                if i in h:
                    h[i]+=1
                else:
                    h[i]=1
        o=0
        ans=-1
        for i in h.keys():
            if h[i]>o:
                o=h[i]
                ans=i
            if h[i]==o and i<ans:
                ans=i
        return ans