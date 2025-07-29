class Solution:
    def solution_1130_3(self, nums: List[int], k: int) -> List[int]:
        i=0
        n=len(nums)
        res_len=0
        stack=[]
        while(i<n):
            while(stack and (n-i)>k-res_len and stack[-1]>nums[i]):
                stack.pop()
                res_len-=1
            else:
                if(res_len<k):
                    stack.append(nums[i])
                    res_len+=1
            i+=1
            
        return stack