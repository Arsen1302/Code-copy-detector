class Solution:
    def solution_123_3(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        answer = [1] * n #this will hold our output
       
		for i in range(0, n):
            for j in range(0, n):
                if i != j:
                    answer[i] = answer[i] * nums[j]
                    
        return answer