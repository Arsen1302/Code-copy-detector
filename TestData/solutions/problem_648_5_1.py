class Solution:
    def solution_648_5_1(self, n: int, k: int) -> List[int]:
        def solution_648_5_2(d, num, i):
            num = num * 10 + d            
            
            if i == n:
                result.append(num)
                return 
            
            if d + k < 10:
                solution_648_5_2(d + k, num, i + 1)
                
            if k > 0 and d - k >= 0:
                solution_648_5_2(d - k, num, i + 1)
            
        result = []
        for d in range(1, 10):
            solution_648_5_2(d, 0, 1)
        
        return result