class Solution:
    def solution_1699_5(self, nums: List[int], k: int) -> int:
        c=0
        for i in range(len(nums)):
            temp=nums[i]
            if temp==k:
                c=c+1
            for j in range(i+1,len(nums)):
                temp=math.gcd(temp,nums[j])
                if temp==k:
                    c=c+1
        
        return c