class Solution:
    def solution_1170_5(self, nums: List[int]) -> int:	
        temp = []
		
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                temp.append(nums[i] * nums[j])
        
        temp = collections.Counter(temp)
        ans = 0
        
        for i, j in temp.items():
            if j >= 2:
                ans += j * (j-1) // 2
        
        return ans * 8