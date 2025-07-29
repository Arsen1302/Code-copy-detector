class Solution:
    def solution_1353_3_1(self, nums: List[str]) -> str:
        
		nums=set(nums)
		
        def solution_1353_3_2(string,depth):
            
            if depth == 0: return string if string not in nums else ""
                
            for value in "01":
                ans=solution_1353_3_2(string+value,depth-1)
                if ans: return ans
				
        return solution_1353_3_2("",len(nums))