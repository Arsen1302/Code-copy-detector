class Solution:
    def solution_920_1(self, n, speed, efficiency):
        
        people = sorted(zip(speed, efficiency), key=lambda x: -x[1])
        
        result, sum_speed = 0, 0
        
        for s, e in people:
            sum_speed += s
            result = max(result, sum_speed * e)
        
        return result # % 1000000007