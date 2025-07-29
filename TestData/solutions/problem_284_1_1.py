class Solution:    
    def solution_284_1_1(self, nums: List[int], target: int) -> int:     
        dic = defaultdict(int)
        
        def solution_284_1_2(index=0, total=0):          
            key = (index, total)
            
            if key not in dic:
                if index == len(nums):                    
                    return 1 if total == target else 0
                else:
                    dic[key] = solution_284_1_2(index+1, total + nums[index]) + solution_284_1_2(index+1, total - nums[index])                    
                        
            return dic[key]                                                             
                
        return solution_284_1_2()