class Solution:
    def solution_671_3(self, startValue: int, target: int) -> int:
        operations = 0
        cpy = target
        while True:
            
            if target <= startValue:
                break
            
            if target %2 == 1:
                target += 1
                operations += 1
                
            target = target // 2           
            operations += 1
        
        way1 = operations + startValue - target
        return way1