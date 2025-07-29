class Solution:
    def solution_1080_2(self, logs: List[str]) -> int:
        res = 0
        
        for i in logs:
            if i == '../' and res > 0:
                res -= 1
            elif i != './' and i != '../':
                res += 1
                
        return res