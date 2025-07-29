class Solution:
    def solution_1699_3_1(self, nums: List[int], k: int) -> int:
        c=0
        for i in range(len(nums)):
            a=nums[i]
            for j in range(i,len(nums)):
                a=solution_1699_3_2(a,nums[j])
                if a==k:
                    c+=1
        return c

def solution_1699_3_2(a,b):
    if b==0:
        return abs(a)
    else:
        return solution_1699_3_2(b,a%b)