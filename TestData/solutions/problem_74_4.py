class Solution:
    def solution_74_4(self, numbers: List[int], target: int) -> List[int]:
        
        seen = {}
        for i, value in enumerate(numbers): 
            remaining = target - numbers[i] 
           
            if remaining in seen: 
                return [seen[remaining]+1, i+1]  #4
            else:
                seen[value] = i