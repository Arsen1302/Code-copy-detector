class Solution:
    def solution_1310_5(self, dist: List[int], speed: List[int]) -> int:
        
        time = [math.ceil(x / y) for x, y in zip(dist, speed)]
        time.sort()
        
        res = 1
        
        for i in range(1, len(time)):
            if time[i] <= res:
                return res
            res += 1
            
        return res