class Solution:
    def solution_114_4_1(self, nums: List[int]) -> List[str]:
        ans, n = [], len(nums)
        
        start = 0
        for i in range(1,n+1):
            if i == n or nums[i] != nums[i-1]+1:
                ans.append(self.solution_114_4_2(nums[start],nums[i-1]))
                start = i
        return ans
    
    def solution_114_4_2(self, a, b):
        return str(a) if a==b else str(a)+"->"+str(b)